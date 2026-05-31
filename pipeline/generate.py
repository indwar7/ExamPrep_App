#!/usr/bin/env python3
"""Exam Tool — open-source explanation-video generator.

End-to-end, 100% free & local:

    question text  --(Qwen via Ollama)-->  derivation_steps
    derivation_steps  --(Manim)-->          per-step animation
    narration         --(Kokoro TTS)-->     per-step voice
    video + voice     --(ffmpeg)-->         one MP4 per question

Usage:
    python generate.py --id q001                 # use steps already in questions.json
    python generate.py --id q001 --regenerate    # ask the LLM for fresh steps
    python generate.py --all                      # build every question
    python generate.py --check                    # verify all tools are installed

No paid APIs. Everything runs on your machine.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from glob import glob
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths & config
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_FILE = ROOT / "questions.json"
OUTPUT_DIR = ROOT / "output"
PIPELINE_DIR = ROOT / "pipeline"
SCENE_FILE = PIPELINE_DIR / "_step_scene.py"

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5:7b")

TTS_VOICE = os.environ.get("KOKORO_VOICE", "af_heart")  # American English, female
TTS_LANG = os.environ.get("KOKORO_LANG", "a")           # 'a' = American English
TTS_SR = 24000                                          # Kokoro output sample rate

MANIM_QUALITY = os.environ.get("MANIM_QUALITY", "-qm")  # -ql 480p / -qm 720p / -qh 1080p


def log(msg: str) -> None:
    print(f"  \033[36m›\033[0m {msg}", flush=True)


def die(msg: str) -> None:
    print(f"\033[31m✗ {msg}\033[0m", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

def check_deps(need_llm: bool = False) -> None:
    missing = []

    if not shutil.which("ffmpeg"):
        missing.append("ffmpeg  ->  brew install ffmpeg")
    try:
        import manim  # noqa: F401
    except ImportError:
        missing.append("manim   ->  pip install -r pipeline/requirements.txt")
    if not shutil.which("latex"):
        log("warning: latex not found — formulas will render as plain text. "
            "For proper math: brew install --cask basictex (then restart shell)")

    try:
        import kokoro  # noqa: F401
    except ImportError:
        missing.append("kokoro  ->  pip install -r pipeline/requirements.txt")

    if not shutil.which("espeak-ng") and not shutil.which("espeak"):
        log("warning: espeak-ng not found — Kokoro may fail on some words "
            "(brew install espeak-ng)")

    if need_llm:
        try:
            import requests
            r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=3)
            tags = [m["name"] for m in r.json().get("models", [])]
            if not any(OLLAMA_MODEL.split(":")[0] in t for t in tags):
                missing.append(
                    f"ollama model '{OLLAMA_MODEL}'  ->  ollama pull {OLLAMA_MODEL}")
        except Exception:
            missing.append(
                "ollama (not running?)  ->  start ollama, then: "
                f"ollama pull {OLLAMA_MODEL}")

    if missing:
        print("\n\033[31mMissing dependencies:\033[0m")
        for m in missing:
            print(f"   • {m}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Step generation (LLM via local Ollama)
# ---------------------------------------------------------------------------

LLM_SYSTEM = (
    "You are a math teacher creating a step-by-step video explanation. "
    "Given a multiple-choice question, produce the derivation as an ordered "
    "list of steps. Each step has:\n"
    "  - 'latex': ONE line of valid LaTeX math (no $ signs, no \\begin/\\end).\n"
    "  - 'narration': one or two spoken sentences explaining that step, "
    "plain text, no symbols (write 'x squared' not 'x^2').\n"
    "The final step must state which option letter is correct. "
    'Return ONLY JSON: {"steps": [{"latex": "...", "narration": "..."}, ...]}'
)


def generate_steps_with_llm(question: dict) -> list[dict]:
    import requests

    opts = "\n".join(f"  {k}: {v}" for k, v in question["options"].items())
    prompt = (
        f"Question: {question['question']}\n"
        f"Options:\n{opts}\n"
        f"Correct answer: option {question['correct']}\n\n"
        "Produce the step-by-step derivation."
    )

    log(f"asking {OLLAMA_MODEL} for derivation steps…")
    resp = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": OLLAMA_MODEL,
            "format": "json",
            "stream": False,
            "options": {"temperature": 0.2},
            "messages": [
                {"role": "system", "content": LLM_SYSTEM},
                {"role": "user", "content": prompt},
            ],
        },
        timeout=300,
    )
    resp.raise_for_status()
    content = resp.json()["message"]["content"]
    steps = json.loads(content).get("steps", [])
    if not steps:
        die("LLM returned no steps")
    log(f"got {len(steps)} steps from LLM")
    return steps


# ---------------------------------------------------------------------------
# TTS (Kokoro, open-source)
# ---------------------------------------------------------------------------

_kokoro_pipeline = None


def _get_kokoro():
    global _kokoro_pipeline
    if _kokoro_pipeline is None:
        from kokoro import KPipeline
        log("loading Kokoro TTS model (first run downloads weights)…")
        _kokoro_pipeline = KPipeline(lang_code=TTS_LANG)
    return _kokoro_pipeline


def synthesize_audio(text: str, out_wav: Path) -> float:
    """Speak `text` to a WAV file. Returns duration in seconds."""
    import numpy as np
    import soundfile as sf

    pipe = _get_kokoro()
    chunks = []
    for result in pipe(text, voice=TTS_VOICE):
        audio = result[-1] if isinstance(result, tuple) else result.audio
        if hasattr(audio, "detach"):       # torch tensor
            audio = audio.detach().cpu().numpy()
        chunks.append(np.asarray(audio, dtype="float32"))

    if not chunks:
        die(f"TTS produced no audio for: {text!r}")

    full = np.concatenate(chunks)
    sf.write(str(out_wav), full, TTS_SR)
    return len(full) / TTS_SR


# ---------------------------------------------------------------------------
# Animation (Manim)
# ---------------------------------------------------------------------------

def render_step_video(latex: str, duration: float, out_mp4: Path, workdir: Path,
                      idx: int) -> None:
    spec_file = workdir / f"spec_{idx}.json"
    spec_file.write_text(json.dumps({"latex": latex, "duration": duration}))

    media_dir = workdir / "manim"
    name = f"step_{idx}"

    env = dict(os.environ, STEP_SPEC=str(spec_file))
    cmd = [
        sys.executable, "-m", "manim", MANIM_QUALITY,
        "--media_dir", str(media_dir),
        "-o", name,
        str(SCENE_FILE), "StepScene",
    ]
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stdout)
        print(res.stderr, file=sys.stderr)
        die(f"manim failed on step {idx}")

    matches = glob(str(media_dir / "videos" / "**" / f"{name}.mp4"), recursive=True)
    if not matches:
        die(f"could not find manim output for step {idx}")
    shutil.move(matches[0], out_mp4)


# ---------------------------------------------------------------------------
# ffmpeg merge
# ---------------------------------------------------------------------------

def _run_ffmpeg(args: list[str], what: str) -> None:
    res = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args],
                         capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stderr, file=sys.stderr)
        die(f"ffmpeg failed: {what}")


def merge_av(video: Path, audio: Path, out: Path) -> None:
    _run_ffmpeg(
        ["-i", str(video), "-i", str(audio),
         "-c:v", "copy", "-c:a", "aac", "-shortest", str(out)],
        "merging step video + audio",
    )


def concat_clips(clips: list[Path], out: Path, workdir: Path) -> None:
    # Re-encode on concat so mismatched params never corrupt the output.
    list_file = workdir / "concat.txt"
    list_file.write_text("".join(f"file '{c}'\n" for c in clips))
    _run_ffmpeg(
        ["-f", "concat", "-safe", "0", "-i", str(list_file),
         "-c:v", "libx264", "-pix_fmt", "yuv420p",
         # normalise + boost the narration so it's clearly audible
         "-af", "loudnorm=I=-14:TP=-1.0:LRA=11",
         "-c:a", "aac", "-b:a", "192k", str(out)],
        "concatenating steps",
    )


# ---------------------------------------------------------------------------
# Build one question
# ---------------------------------------------------------------------------

def build_video(question: dict, regenerate: bool) -> Path:
    qid = question["id"]
    print(f"\n\033[1m▶ Building {qid}\033[0m — {question['question']}")

    steps = question.get("derivation_steps")
    if regenerate or not steps:
        steps = generate_steps_with_llm(question)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / f"{qid}.mp4"

    with tempfile.TemporaryDirectory(prefix=f"examtool_{qid}_") as tmp:
        workdir = Path(tmp)
        step_clips = []

        for i, step in enumerate(steps):
            log(f"step {i + 1}/{len(steps)}: {step['latex']}")
            audio = workdir / f"audio_{i}.wav"
            video = workdir / f"video_{i}.mp4"
            clip = workdir / f"clip_{i}.mp4"

            dur = synthesize_audio(step["narration"], audio)
            render_step_video(step["latex"], dur + 0.4, video, workdir, i)
            merge_av(video, audio, clip)
            step_clips.append(clip)

        log("stitching final video…")
        concat_clips(step_clips, out_path, workdir)

    print(f"\033[32m✓ {out_path}\033[0m")
    return out_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def load_questions() -> list[dict]:
    if not QUESTIONS_FILE.exists():
        die(f"{QUESTIONS_FILE} not found")
    return json.loads(QUESTIONS_FILE.read_text())["questions"]


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate explanation videos (all open-source).")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--id", help="build a single question by id, e.g. q001")
    g.add_argument("--all", action="store_true", help="build every question")
    ap.add_argument("--regenerate", action="store_true",
                    help="generate derivation_steps with the LLM instead of using questions.json")
    ap.add_argument("--check", action="store_true",
                    help="check that all tools are installed, then exit")
    args = ap.parse_args()

    if args.check:
        check_deps(need_llm=True)
        print("\033[32m✓ all dependencies look good\033[0m")
        return

    if not args.id and not args.all:
        ap.error("pass --id <qid>, --all, or --check")

    check_deps(need_llm=args.regenerate)

    questions = load_questions()
    if args.all:
        targets = questions
    else:
        targets = [q for q in questions if q["id"] == args.id]
        if not targets:
            die(f"no question with id '{args.id}'")

    for q in targets:
        build_video(q, regenerate=args.regenerate)


if __name__ == "__main__":
    main()
