#!/usr/bin/env python3
"""
Add narration to quiz explanation videos
Uses macOS 'say' command to generate audio from text
"""

import os
import subprocess
import shutil

VIDEO_DIR = "/Users/abhayindwar/Desktop/examtool/video"
AUDIO_DIR = "/tmp/narration_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Narration text for each video
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

def generate_audio(text, output_file):
    """Generate audio using macOS say command"""
    print(f"Generating audio: {os.path.basename(output_file)}")

    # Use say command to generate MP3
    cmd = [
        'say',
        '-r', '150',  # Speaking rate
        '-o', output_file,
        '--file-format=mp3',
        '--quality=127',
        text
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"  ✅ Audio created: {output_file}")
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def merge_audio_video(video_file, audio_file, output_file):
    """Merge audio and video using ffmpeg"""
    print(f"Merging audio with video: {os.path.basename(output_file)}")

    cmd = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-map', '0:v:0',
        '-map', '1:a:0',
        '-shortest',
        '-y',
        output_file
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"  ✅ Video with audio created: {output_file}")
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    print("\n" + "="*60)
    print("ADDING NARRATION TO VIDEOS")
    print("="*60 + "\n")

    success_count = 0

    for video_base, narration_text in NARRATIONS.items():
        print(f"\nProcessing: {video_base}")
        print(f"Narration: {narration_text[:50]}...")

        # Original video file
        video_file = os.path.join(VIDEO_DIR, f"{video_base}.mp4")

        # Generate audio
        audio_file = os.path.join(AUDIO_DIR, f"{video_base}.mp3")
        if generate_audio(narration_text, audio_file):
            # Merge audio with video
            output_file = os.path.join(VIDEO_DIR, f"{video_base}_narrated.mp4")
            if merge_audio_video(video_file, audio_file, output_file):
                # Replace original with narrated version
                shutil.move(output_file, video_file)
                print(f"  ✅ Original video updated with narration")
                success_count += 1

        print()

    print("="*60)
    print(f"✅ COMPLETED: {success_count}/10 videos updated with narration")
    print("="*60)

    # Cleanup
    import shutil
    shutil.rmtree(AUDIO_DIR, ignore_errors=True)
    print("\n✨ Narration audio files cleaned up")

if __name__ == "__main__":
    main()
