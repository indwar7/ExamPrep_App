#!/usr/bin/env python3
"""Add narration to videos using macOS say command"""

import os
import subprocess
import shutil

VIDEO_DIR = "/Users/abhayindwar/Desktop/examtool/video"
AUDIO_DIR = "/tmp/narration_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

NARRATIONS = {
    "q001-correct": "Question: What is science? Answer: B. Science is a systematic process of observing, questioning, testing, and learning.",
    "q001-incorrect": "Question: What is science? Your answer is incorrect. The correct answer is B. Science is a process, not just facts to memorize.",
    "q002-correct": "Question: First step of scientific method? Answer: B - Observe. Observation is the foundation of all science.",
    "q002-incorrect": "Question: First step of scientific method? Your answer is incorrect. The correct answer is B - Observe. Always start with careful observation.",
    "q003-correct": "Question: Science in everyday life? Answer: D - All of the above. Science happens everywhere, in cooking, sports, gardening, and medicine.",
    "q003-incorrect": "Question: Science in everyday life? Your answer is incomplete. The correct answer is D - All of the above.",
    "q004-correct": "Question: Steps in scientific method? Answer: C - exactly 5 steps. Observe, Question, Hypothesis, Test, and Analyze.",
    "q004-incorrect": "Question: Steps in scientific method? Your answer is incorrect. The correct answer is C - exactly 5 steps, no more, no less.",
    "q005-correct": "Question: Can anyone be a scientist? Answer: B - YES! If you observe, question, and test ideas, you are a scientist.",
    "q005-incorrect": "Question: Can anyone be a scientist? Your answer is incorrect. The correct answer is B - YES! Anyone can think scientifically and be a scientist.",
}

def generate_narration(text, output_aiff):
    """Generate audio using say command"""
    cmd = ['say', '-o', output_aiff, text]
    subprocess.run(cmd, check=True, capture_output=True)

def merge_with_ffmpeg(video, audio, output):
    """Merge audio and video"""
    cmd = [
        'ffmpeg',
        '-i', video,
        '-i', audio,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-map', '0:v:0',
        '-map', '1:a:0',
        '-shortest',
        '-y',
        output
    ]
    subprocess.run(cmd, check=True, capture_output=True)

print("\n" + "="*60)
print("ADDING NARRATION TO VIDEOS")
print("="*60 + "\n")

success = 0

for video_name, text in NARRATIONS.items():
    try:
        print(f"Processing: {video_name}")

        # Paths
        video_file = f"{VIDEO_DIR}/{video_name}.mp4"
        audio_file = f"{AUDIO_DIR}/{video_name}.aiff"
        temp_output = f"{AUDIO_DIR}/{video_name}_with_audio.mp4"

        # Generate narration
        generate_narration(text, audio_file)
        print(f"  ✅ Audio generated")

        # Merge audio with video
        merge_with_ffmpeg(video_file, audio_file, temp_output)
        print(f"  ✅ Audio merged with video")

        # Replace original
        shutil.move(temp_output, video_file)
        print(f"  ✅ Video updated with narration\n")
        success += 1

    except Exception as e:
        print(f"  ❌ Error: {e}\n")

print("="*60)
print(f"✅ COMPLETED: {success}/10 videos")
print("="*60)

# Cleanup
shutil.rmtree(AUDIO_DIR, ignore_errors=True)
