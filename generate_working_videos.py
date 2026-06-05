#!/usr/bin/env python3
"""
Generate working MP4 videos for quiz explanations
Creates proper video files that actually display
"""

import subprocess
import os

VIDEO_DIR = "/Users/abhayindwar/Desktop/examtool/video"
os.makedirs(VIDEO_DIR, exist_ok=True)

# Question explanations
EXPLANATIONS = {
    "q001-correct": "Q: What is science?\n\nAnswer: B\n\nWhy correct:\nScience = Systematic thinking\nObserve, Question, Test, Learn!",
    "q001-incorrect": "Q: What is science?\n\nYour answer: INCORRECT\n\nCorrect answer: B\n\nScience is a PROCESS, not facts!",

    "q002-correct": "Q: First step of scientific method?\n\nAnswer: B - OBSERVE\n\nObservation is the FOUNDATION!",
    "q002-incorrect": "Q: First step of scientific method?\n\nYour answer: INCORRECT\n\nCorrect: B - OBSERVE always first!",

    "q003-correct": "Q: Science in everyday life?\n\nAnswer: D - ALL of the above\n\nScience is EVERYWHERE!",
    "q003-incorrect": "Q: Science in everyday life?\n\nYour answer: INCOMPLETE\n\nCorrect: D - All professions use science",

    "q004-correct": "Q: Steps in scientific method?\n\nAnswer: C - 5 steps\n\n1. Observe\n2. Question\n3. Hypothesis\n4. Test\n5. Analyze",
    "q004-incorrect": "Q: Steps in scientific method?\n\nYour answer: INCORRECT\n\nCorrect: C - EXACTLY 5 steps always!",

    "q005-correct": "Q: Can anyone be a scientist?\n\nAnswer: B - YES!\n\nIf you observe, question, test = scientist!",
    "q005-incorrect": "Q: Can anyone be a scientist?\n\nYour answer: INCORRECT\n\nCorrect: B - YES, if you think scientifically!",
}

def create_video_with_text(filename, text):
    """Create MP4 video using ffmpeg with text overlay"""
    output_path = f"{VIDEO_DIR}/{filename}.mp4"

    # Create a 6-second video with text using ffmpeg
    # Using color filter with drawtext
    cmd = [
        'ffmpeg',
        '-f', 'lavfi',
        '-i', f'color=c=white:s=1920x1080:d=6',  # 6 second white background
        '-vf', f'drawtext=text=\'{text}\':fontsize=60:fontcolor=black:x=100:y=100:font=Arial',
        '-pix_fmt', 'yuv420p',
        '-c:v', 'libx264',
        '-preset', 'ultrafast',
        '-y',
        output_path
    ]

    print(f"Creating: {filename}.mp4")
    try:
        subprocess.run(cmd, capture_output=True, check=True, timeout=30)
        print(f"  ✅ Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Error: {e}")
        return False
    except subprocess.TimeoutExpired:
        print(f"  ❌ Timeout")
        return False

def main():
    print("\n" + "="*60)
    print("🎬 CREATING WORKING VIDEOS")
    print("="*60 + "\n")

    success = 0
    for filename, text in EXPLANATIONS.items():
        if create_video_with_text(filename, text):
            success += 1

    print("\n" + "="*60)
    print(f"✅ Created {success}/{len(EXPLANATIONS)} videos")
    print("="*60)

    print(f"\n✨ Videos in: {VIDEO_DIR}\n")

    # List files
    files = [f for f in os.listdir(VIDEO_DIR) if f.endswith('.mp4')]
    for f in sorted(files):
        size = os.path.getsize(f"{VIDEO_DIR}/{f}") / 1024
        print(f"  ✅ {f} ({size:.0f} KB)")

if __name__ == "__main__":
    main()
