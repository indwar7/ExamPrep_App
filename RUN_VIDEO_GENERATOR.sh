#!/bin/bash

echo "🎬 WHITEBOARD VIDEO GENERATOR - SETUP & RUN"
echo "==========================================="
echo ""

# Check if ffmpeg is installed
echo "Checking ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ ffmpeg not found"
    echo ""
    echo "Installing ffmpeg..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        echo "Installing via Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        brew install ffmpeg
    else
        echo "Please install ffmpeg first:"
        echo "  Ubuntu/Debian: sudo apt-get install ffmpeg"
        echo "  Fedora: sudo dnf install ffmpeg"
        echo "  Windows: choco install ffmpeg"
        exit 1
    fi
else
    echo "✅ ffmpeg installed"
fi

echo ""

# Check if PIL is installed
echo "Checking Python dependencies..."
python3 -c "from PIL import Image" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing Pillow (PIL)..."
    pip3 install Pillow
else
    echo "✅ Pillow installed"
fi

echo ""
echo "=========================================="
echo "🎬 Starting video generation..."
echo "=========================================="
echo ""

# Run the video generator
cd /Users/abhayindwar/Desktop/examtool
python3 generate_whiteboard_videos.py

echo ""
echo "Done! Check /Users/abhayindwar/Desktop/examtool/video/ for MP4 files"
