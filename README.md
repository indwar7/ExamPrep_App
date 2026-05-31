# Exam Tool

MCQ exam app where wrong answers trigger an instant step-by-step video explanation (Khan Academy / 3Blue1Brown style).

## Structure

```
examtool/
├── questions.json      # Question bank (MVP — graduates to DB later)
├── pipeline/           # Manim + TTS + ffmpeg video generation
│   ├── generate.py     # (TODO) Builds MP4 from a question's derivation_steps
│   └── requirements.txt
├── output/             # Generated MP4s land here (then upload to S3/R2)
└── app/                # (TODO) Flutter quiz frontend
```

## Question schema

Each question in `questions.json`:

| Field | Notes |
|---|---|
| `id` | Stable string, e.g. `q001` |
| `subject` / `topic` / `difficulty` | For filtering / analytics |
| `question` | Plain text shown to user |
| `options` | `{A, B, C, D}` map |
| `correct` | Letter key into `options` |
| `derivation_steps` | Array of `{latex, narration}` — each becomes one animated step with synced voice |

The pipeline reads `derivation_steps`, renders Manim animation + TTS audio per step, stitches via ffmpeg, outputs one MP4 per question.

## Flow

**Authoring time (offline, slow):**
```
question + derivation_steps  →  Manim render  +  TTS  →  ffmpeg merge  →  MP4  →  CDN
```

**Quiz time (instant, ~50ms):**
```
user picks wrong option  →  fetch video_url  →  play MP4
```

## Setup (all open-source, local)

```bash
brew install ffmpeg espeak-ng pango pkg-config cairo python@3.12 ollama
ollama serve &                 # start the local LLM server
ollama pull qwen2.5:7b         # math-capable open model

python3.12 -m venv .venv
.venv/bin/pip install -r pipeline/requirements.txt

# LaTeX for proper math rendering (needs your password):
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install standalone preview doublestroke dvisvgm physics
# restart your shell, then check:
.venv/bin/python pipeline/generate.py --check
```

## Run

```bash
.venv/bin/python pipeline/generate.py --id q004              # build one question
.venv/bin/python pipeline/generate.py --id q004 --regenerate # LLM writes fresh steps
.venv/bin/python pipeline/generate.py --all                  # build everything
```

Output lands in `output/<id>.mp4`.

## Status

MVP pipeline works end-to-end (Qwen → Manim → Kokoro → ffmpeg), fully open-source.
Without LaTeX installed, formulas fall back to plain text; install BasicTeX for
proper math rendering.
