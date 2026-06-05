#!/bin/bash

# Create simple working videos for quiz explanations
VIDEO_DIR="/Users/abhayindwar/Desktop/examtool/video"

mkdir -p "$VIDEO_DIR"

echo "🎬 Creating working videos..."

# Create 10 simple videos (white background, playable, 6 seconds each)
for i in {1..5}; do
    # Correct video
    ffmpeg -f lavfi -i color=white:s=1920x1080:d=6 \
        -f lavfi -i anullsrc=r=44100:cl=mono \
        -c:v libx264 -c:a aac -pix_fmt yuv420p -y \
        "$VIDEO_DIR/q00$i-correct.mp4" 2>/dev/null

    echo "  ✅ q00$i-correct.mp4"

    # Incorrect video
    ffmpeg -f lavfi -i color=white:s=1920x1080:d=6 \
        -f lavfi -i anullsrc=r=44100:cl=mono \
        -c:v libx264 -c:a aac -pix_fmt yuv420p -y \
        "$VIDEO_DIR/q00$i-incorrect.mp4" 2>/dev/null

    echo "  ✅ q00$i-incorrect.mp4"
done

echo ""
echo "✅ All videos created!"
ls -lh "$VIDEO_DIR"/*.mp4 2>/dev/null | awk '{print "   " $9 " (" $5 ")"}'
