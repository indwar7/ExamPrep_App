#!/usr/bin/env python3
"""
Whiteboard Video Generator
Automatically creates explanation videos with white background and black pen
"""

import os
from PIL import Image, ImageDraw, ImageFont
import subprocess
import shutil

# Configuration
VIDEO_OUTPUT_DIR = "/Users/abhayindwar/Desktop/examtool/video"
FRAME_DURATION = 100  # milliseconds per frame
FPS = 30
RESOLUTION = (1920, 1080)

# Ensure video directory exists
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)

# Question data with explanations
QUESTIONS = {
    "q001": {
        "type": "correct",
        "question": "What is science?",
        "answer": "B",
        "explanation": [
            "Q: What is science?",
            "",
            "Answer: B",
            "",
            "Why B is correct:",
            "",
            "Science is NOT just memorized facts.",
            "It's a PROCESS - a way of thinking.",
            "",
            "The Scientific Method:",
            "1. Observe - Gather information",
            "2. Question - Ask why/how",
            "3. Hypothesis - Make prediction",
            "4. Test - Design experiment",
            "5. Analyze - Interpret results",
            "",
            "Science happens EVERYWHERE:",
            "* In kitchens (cooking = chemistry)",
            "* In sports (movement = physics)",
            "* In gardens (plants = biology)",
            "",
            "Key Point:",
            "Science = Systematic Thinking"
        ]
    },
    "q001_incorrect": {
        "type": "incorrect",
        "question": "What is science?",
        "answer": "NOT B",
        "explanation": [
            "Q: What is science?",
            "",
            "Your answer was INCORRECT",
            "",
            "Correct Answer: B",
            "",
            "Why your answer was wrong:",
            "",
            "A) WRONG - Science is not just",
            "   facts to memorize",
            "",
            "C) WRONG - Science doesn't only",
            "   happen in laboratories",
            "",
            "D) WRONG - Anyone can be a scientist",
            "   (not just 'smart people')",
            "",
            "Why B is CORRECT:",
            "Science = Systematic Process of",
            "Observing, Questioning, Testing,",
            "and Learning",
            "",
            "This is what defines SCIENCE!"
        ]
    },
    "q002": {
        "type": "correct",
        "question": "First step of scientific method?",
        "answer": "B",
        "explanation": [
            "Q: First step of scientific method?",
            "",
            "Answer: B",
            "Observe carefully and gather info",
            "",
            "Why B is CORRECT:",
            "",
            "OBSERVATION is the FOUNDATION",
            "of all science!",
            "",
            "The Scientific Method Order:",
            "1. OBSERVE ← START HERE (ALWAYS!)",
            "2. Question",
            "3. Hypothesis",
            "4. Test",
            "5. Analyze",
            "",
            "You CANNOT skip observation!",
            "",
            "Examples of observation:",
            "* Watch water boil",
            "* Notice plant growth",
            "* See colors in rainbow",
            "",
            "Key Point:",
            "ALL science begins with",
            "CAREFUL OBSERVATION"
        ]
    },
    "q002_incorrect": {
        "type": "incorrect",
        "question": "First step of scientific method?",
        "answer": "NOT B",
        "explanation": [
            "Q: First step of scientific method?",
            "",
            "Your answer was INCORRECT",
            "",
            "Correct Answer: B",
            "Observe carefully and gather info",
            "",
            "OBSERVATION is ALWAYS step 1!",
            "",
            "The Right Order:",
            "1. Observe ← MUST START HERE",
            "2. Question",
            "3. Hypothesis",
            "4. Test",
            "5. Analyze",
            "",
            "You cannot:",
            "- Start with a hypothesis",
            "- Begin testing",
            "- Skip to conclusions",
            "",
            "WITHOUT first observing!",
            "",
            "Remember:",
            "OBSERVATION = Foundation",
            "of ALL science"
        ]
    },
    "q003": {
        "type": "correct",
        "question": "Science in everyday life?",
        "answer": "D",
        "explanation": [
            "Q: Science in everyday life?",
            "",
            "Answer: D - All of the above",
            "",
            "Why D is CORRECT:",
            "",
            "Science is EVERYWHERE!",
            "Not just in laboratories.",
            "",
            "Real Examples:",
            "",
            "* Chef cooking",
            "  = Chemistry (heat changes food)",
            "",
            "* Mechanic fixing cars",
            "  = Physics (how machines work)",
            "",
            "* Farmer growing plants",
            "  = Biology (plant growth/nutrients)",
            "",
            "* Doctor treating patients",
            "  = Medical Science",
            "",
            "* Athlete in sports",
            "  = Physics (movement/forces)",
            "",
            "Key Truth:",
            "Science is a universal way of",
            "thinking used by EVERYONE"
        ]
    },
    "q003_incorrect": {
        "type": "incorrect",
        "question": "Science in everyday life?",
        "answer": "NOT D",
        "explanation": [
            "Q: Science in everyday life?",
            "",
            "Your answer was INCOMPLETE",
            "",
            "Correct Answer: D",
            "All of the above",
            "",
            "You were PARTIALLY correct, but",
            "missed the bigger picture!",
            "",
            "The Truth:",
            "",
            "Science happens in:",
            "- Cooking (A)",
            "- Mechanics (B)",
            "- Farming (C)",
            "",
            "PLUS many other places!",
            "",
            "Science is NOT limited to one",
            "profession or activity.",
            "",
            "It's a UNIVERSAL way of",
            "thinking used by everyone:",
            "- Teachers",
            "- Builders",
            "- Artists",
            "- Everyone!",
            "",
            "Key Point:",
            "Science = Universal Thinking"
        ]
    },
    "q004": {
        "type": "correct",
        "question": "Steps in scientific method?",
        "answer": "C",
        "explanation": [
            "Q: How many steps in the",
            "   scientific method?",
            "",
            "Answer: C - 5 steps",
            "",
            "Why C is CORRECT:",
            "",
            "The Scientific Method has",
            "EXACTLY 5 steps:",
            "",
            "1. OBSERVE",
            "   Gather information carefully",
            "",
            "2. QUESTION",
            "   Ask why/how",
            "",
            "3. HYPOTHESIS",
            "   Make a prediction",
            "",
            "4. TEST",
            "   Design and conduct experiment",
            "",
            "5. ANALYZE",
            "   Interpret the results",
            "",
            "Important:",
            "- These steps are ALWAYS done",
            "- In THIS order",
            "- ALL 5 are ESSENTIAL",
            "- No shortcuts!",
            "",
            "Scientists worldwide use",
            "this exact 5-step process"
        ]
    },
    "q004_incorrect": {
        "type": "incorrect",
        "question": "Steps in scientific method?",
        "answer": "NOT C",
        "explanation": [
            "Q: How many steps in the",
            "   scientific method?",
            "",
            "Your answer was INCORRECT",
            "",
            "Correct Answer: C",
            "EXACTLY 5 steps",
            "",
            "The 5 Scientific Method Steps:",
            "",
            "1. Observe",
            "2. Question",
            "3. Hypothesis",
            "4. Test",
            "5. Analyze",
            "",
            "NOT 3, NOT 4, NOT 6",
            "",
            "ALWAYS exactly 5!",
            "",
            "No variations",
            "No shortcuts",
            "No exceptions",
            "",
            "Whether you're:",
            "- Testing a cake recipe",
            "- Studying plants",
            "- Experimenting with physics",
            "",
            "The 5 steps are",
            "UNIVERSAL and MANDATORY"
        ]
    },
    "q005": {
        "type": "correct",
        "question": "Can anyone be a scientist?",
        "answer": "B",
        "explanation": [
            "Q: Can anyone be a scientist?",
            "",
            "Answer: B - YES!",
            "If you observe, question, and test",
            "",
            "Why B is CORRECT:",
            "",
            "Science is a WAY OF THINKING",
            "NOT a job title or profession!",
            "",
            "Requirements to be a scientist:",
            "",
            "What you DON'T need:",
            "- NO degree required",
            "- NO laboratory needed",
            "- NO special permission",
            "- NO age limit",
            "",
            "What you DO need:",
            "- Curiosity",
            "- Willingness to observe",
            "- Desire to test ideas",
            "- Openness to learn",
            "",
            "Examples of scientists:",
            "- Students doing experiments",
            "- Children exploring nature",
            "- Adults trying new recipes",
            "- Anyone thinking systematically",
            "",
            "Key Truth:",
            "SCIENCE IS FOR EVERYONE!",
            "You are already a scientist"
            "when you think scientifically"
        ]
    },
    "q005_incorrect": {
        "type": "incorrect",
        "question": "Can anyone be a scientist?",
        "answer": "NOT B",
        "explanation": [
            "Q: Can anyone be a scientist?",
            "",
            "Your answer was INCORRECT",
            "",
            "Correct Answer: B",
            "YES - If you observe, question,",
            "and test",
            "",
            "Why your answer was wrong:",
            "",
            "A) WRONG - You don't need a",
            "   degree to be a scientist",
            "",
            "C) WRONG - You don't need a",
            "   laboratory",
            "",
            "D) WRONG - Any age can be a",
            "   scientist",
            "",
            "The Real Truth:",
            "",
            "Science = Systematic thinking",
            "",
            "If you:",
            "- Observe carefully",
            "- Ask questions",
            "- Test your ideas",
            "- Learn from results",
            "",
            "THEN YOU ARE A SCIENTIST!",
            "",
            "Age doesn't matter",
            "Credentials don't matter",
            "Education level doesn't matter",
            "",
            "Your THINKING STYLE matters!"
        ]
    }
}

def create_frame(text_lines, frame_number, total_frames):
    """Create a single frame image"""
    # Create white background
    img = Image.new('RGB', RESOLUTION, color='white')
    draw = ImageDraw.Draw(img)

    # Try to load font, fall back to default if not available
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 45)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 35)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Determine how many lines to show (progressive reveal)
    lines_to_show = min(int((frame_number / total_frames) * len(text_lines)), len(text_lines))

    # Draw text
    y_position = 80
    for i, line in enumerate(text_lines[:lines_to_show]):
        if line.startswith("Q:"):
            font = font_large
            color = 'black'
        elif line.startswith("Answer:") or line.startswith("Your answer"):
            font = font_medium
            color = 'darkred' if "INCORRECT" in line else 'darkgreen'
        elif line.startswith(("1.", "2.", "3.", "4.", "5.", "*", "-")):
            font = font_small
            color = 'black'
        else:
            font = font_small
            color = 'black'

        draw.text((100, y_position), line, fill=color, font=font)
        y_position += 70

    return img

def create_video(question_key, question_data):
    """Generate video for a question"""
    frames = []
    total_frames = 120  # 4 seconds at 30 FPS

    print(f"Generating frames for {question_key}...")

    # Create frames
    for frame_num in range(total_frames):
        frame = create_frame(question_data['explanation'], frame_num, total_frames)
        frames.append(frame)

    # Add hold frames at the end
    for _ in range(60):  # 2 second hold at end
        frames.append(frames[-1])

    # Save frames as temporary images
    temp_dir = f"/tmp/video_frames_{question_key}"
    os.makedirs(temp_dir, exist_ok=True)

    print(f"Saving {len(frames)} frames...")
    for i, frame in enumerate(frames):
        frame.save(f"{temp_dir}/frame_{i:04d}.png")

    # Create video from frames using ffmpeg
    output_file = f"{VIDEO_OUTPUT_DIR}/{question_key}.mp4"

    print(f"Creating video file: {output_file}...")

    ffmpeg_cmd = [
        'ffmpeg',
        '-y',  # Overwrite if exists
        '-framerate', '30',
        '-i', f'{temp_dir}/frame_%04d.png',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-q:v', '5',
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, capture_output=True, check=True)
        print(f"✅ Created: {output_file}")

        # Cleanup
        shutil.rmtree(temp_dir)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating video: {e}")
        print("Make sure ffmpeg is installed: brew install ffmpeg")
        return False

def main():
    print("\n" + "="*60)
    print("🎬 WHITEBOARD VIDEO GENERATOR")
    print("="*60 + "\n")

    # Check if ffmpeg is installed
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("✅ ffmpeg found\n")
    except:
        print("❌ ERROR: ffmpeg not installed!")
        print("\nInstall ffmpeg:")
        print("  Mac: brew install ffmpeg")
        print("  Windows: choco install ffmpeg")
        print("  Linux: sudo apt-get install ffmpeg")
        print("\nThen try again!\n")
        return

    print(f"Output directory: {VIDEO_OUTPUT_DIR}\n")

    # Generate all videos
    success_count = 0
    for question_key, question_data in QUESTIONS.items():
        if create_video(question_key, question_data):
            success_count += 1

    print("\n" + "="*60)
    print(f"✅ Generated {success_count}/{len(QUESTIONS)} videos")
    print("="*60)

    print(f"\n📁 Videos saved in: {VIDEO_OUTPUT_DIR}")
    print("\nVideos created:")
    for filename in sorted(os.listdir(VIDEO_OUTPUT_DIR)):
        if filename.endswith('.mp4'):
            print(f"  ✅ {filename}")

    print("\n🎯 Next steps:")
    print("1. Open http://localhost:8000/phase4-interactive-app.html")
    print("2. Go to Quiz tab")
    print("3. Answer a question")
    print("4. Watch the explanation video!")
    print("\n")

if __name__ == "__main__":
    main()
