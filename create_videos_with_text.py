#!/usr/bin/env python3
"""Create MP4 videos with text explanation using PIL and ffmpeg"""

import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

VIDEO_DIR = "/Users/abhayindwar/Desktop/examtool/video"
os.makedirs(VIDEO_DIR, exist_ok=True)

def create_video_with_text(output_file, text_lines):
    """Create a 6-second video with white background and black text"""

    # Create frames directory
    frames_dir = f"/tmp/video_frames_{os.path.basename(output_file)}"
    os.makedirs(frames_dir, exist_ok=True)

    # Create 180 frames (30 fps * 6 seconds)
    img_width, img_height = 1280, 720

    # Create image with white background and text
    img = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(img)

    # Try to load a nice font, fallback to default
    try:
        font_large = ImageFont.truetype("/Library/Fonts/Arial.ttf", 48)
        font_small = ImageFont.truetype("/Library/Fonts/Arial.ttf", 36)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Draw text
    y_pos = 100
    for line in text_lines:
        if line.startswith("Q:") or line.startswith("Answer:"):
            draw.text((80, y_pos), line, fill='black', font=font_large)
            y_pos += 80
        else:
            draw.text((80, y_pos), line, fill='black', font=font_small)
            y_pos += 60

    # Save the image 180 times (for 6 seconds at 30fps)
    frame_path = os.path.join(frames_dir, "frame.png")
    img.save(frame_path)

    # Create video using ffmpeg
    cmd = [
        'ffmpeg',
        '-loop', '1',
        '-i', frame_path,
        '-f', 'lavfi',
        '-i', 'sine=frequency=1000:duration=6',
        '-c:v', 'libx264',
        '-t', '6',
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac',
        '-y',
        output_file
    ]

    subprocess.run(cmd, capture_output=True, check=True)

    # Clean up
    import shutil
    shutil.rmtree(frames_dir, ignore_errors=True)

    return output_file

# Create videos
print("Creating Q1 videos with text...")

q1_correct_text = [
    "Q: What is science?",
    "",
    "Answer: B",
    "",
    "Science = Systematic thinking",
    "Observe, Question, Test, Learn!"
]

q1_incorrect_text = [
    "Q: What is science?",
    "",
    "Your answer: INCORRECT",
    "",
    "Correct: B",
    "Science is a PROCESS not facts!"
]

try:
    create_video_with_text(
        f"{VIDEO_DIR}/q001-correct.mp4",
        q1_correct_text
    )
    print("✅ q001-correct.mp4 created")
except Exception as e:
    print(f"❌ Error: {e}")

try:
    create_video_with_text(
        f"{VIDEO_DIR}/q001-incorrect.mp4",
        q1_incorrect_text
    )
    print("✅ q001-incorrect.mp4 created")
except Exception as e:
    print(f"❌ Error: {e}")

# Verify
print("\nVerifying videos...")
for f in [f"{VIDEO_DIR}/q001-correct.mp4", f"{VIDEO_DIR}/q001-incorrect.mp4"]:
    result = os.path.getsize(f) / 1024 / 1024
    print(f"  {os.path.basename(f)}: {result:.1f} MB")
