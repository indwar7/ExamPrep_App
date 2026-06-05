# 🚀 Quick Start - 5 Minutes to Working Platform

## Step 1: Get ElevenLabs API Key (2 min)

```bash
# Visit this link
https://elevenlabs.io/app/sign-up

# After signup, get API key from:
Settings → API Keys → Copy your key
```

## Step 2: Start Backend (1 min)

```bash
# In terminal, navigate to project folder
cd /Users/abhayindwar/Desktop/examtool

# Install dependencies
pip install -r requirements.txt

# Start server with your API key
export ELEVENLABS_API_KEY="sk_abc123..." && python run_server.py
```

You'll see:
```
✅ API Key found!
🌐 Open browser: http://localhost:5000
```

## Step 3: Open the Platform (1 min)

Open this file in your browser:
```
ai-content-platform.html
```

Or open URL:
```
http://localhost:5000/ai-content-platform.html
```

## Step 4: Configure & Generate (1 min)

1. **Click "Configure API"** button (top right)
2. **Paste your ElevenLabs API key**
3. **Click "Save Configuration"**

4. **Select a chapter:**
   - Class: 6
   - Subject: Science
   - Chapter: Food: Where Does It Come From?

5. **Click "Generate Content"**

Wait 30-60 seconds... then you'll see:

✅ **Videos** tab: AI-generated experiment videos
✅ **Audiobook** tab: Full chapter narration (with play/pause/speed control)
✅ **Notes** tab: Quick summary
✅ **Content** tab: Full chapter (download as PDF/Word)

## What's Happening Behind the Scenes?

```
┌─────────────────────────────────────┐
│  Your Browser                       │
│  Select Chapter → Click Generate    │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│  Backend (Flask Server)             │
│  1. Extract experiments from text   │
│  2. Generate videos (ElevenLabs)    │
│  3. Convert to audiobook (ElevenLabs TTS)
│  4. Format as notes & summary       │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│  ElevenLabs API                     │
│  • Text-to-Video (AI videos)        │
│  • Text-to-Speech (Natural voices)  │
└─────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│  Back to Your Browser               │
│  ✓ Videos ready to play             │
│  ✓ Audio ready to listen            │
│  ✓ All formats generated            │
└─────────────────────────────────────┘
```

## Troubleshooting

### Issue: "API Key not configured"
**Solution**: 
1. Click "Configure API"
2. Make sure you paste the FULL key (starts with `sk_`)
3. Click "Save"

### Issue: "No videos generated"
**Solution**:
1. Check your API key is valid in ElevenLabs dashboard
2. Verify you have API credits
3. Check browser console (F12 → Console tab) for errors

### Issue: "Server won't start"
**Solution**:
```bash
# Make sure dependencies are installed
pip install -r requirements.txt

# Make sure API key is set
export ELEVENLABS_API_KEY="your_key_here"

# Try running directly
python content_generator.py
```

### Issue: "Audio not playing"
**Solution**:
1. Try a different browser (Chrome preferred)
2. Clear browser cache (Ctrl+Shift+Delete)
3. Check audio file was generated (check server logs)

## Next Steps

### 1. **Test with Different Chapters**
```
Class 6 → Science → Different chapters
Class 7 → Different subjects
Class 8, 9 → Add more content
```

### 2. **Customize Content**
Edit `content_generator.py` to change:
- Document structure
- Summary format
- Illustration types
- Voice settings

### 3. **Batch Generation**
Create a script to generate all chapters:
```python
chapters = [
    ("6", "science", "Food: Where Does It Come From?"),
    ("6", "science", "Components of Food"),
    ("6", "math", "Knowing Our Numbers"),
]

for class_level, subject, chapter in chapters:
    # Generate content for each
```

### 4. **Deploy Online**
```bash
# Option 1: Vercel (frontend)
vercel

# Option 2: Heroku (backend)
heroku create && git push heroku main

# Option 3: Self-hosted
gunicorn -w 4 app:app
```

## File Structure

```
examtool/
├── ai-content-platform.html      # Beautiful UI
├── content_generator.py           # Backend logic
├── run_server.py                  # Start server
├── requirements.txt               # Dependencies
├── SETUP_GUIDE.md                # Full documentation
└── QUICK_START.md                # This file
```

## Key Features

✅ **Beautiful, Modern UI**
- Dark theme with gradients
- Smooth animations
- Responsive design
- Professional look

✅ **AI Video Generation**
- Automatic experiment video creation
- Step-by-step demonstrations
- Multiple chunks for long content
- MP4 ready-to-use format

✅ **Professional Audiobook**
- Natural sounding narration
- Speed control (0.75x - 2x)
- Professional TTS voice
- High quality MP3

✅ **Multiple Formats**
- Detailed Word/PDF documents
- Quick reference notes
- Illustration guides
- Full chapter content

✅ **Easy to Extend**
- Add new chapters in seconds
- Customize voice/style
- Batch generation ready
- API-driven architecture

## Support Resources

- **ElevenLabs Docs**: https://elevenlabs.io/docs
- **API Reference**: https://elevenlabs.io/docs/api-reference
- **Voice Gallery**: https://elevenlabs.io/voice-lab

## Pro Tips

💡 **Tip 1**: Generate content during off-peak hours to avoid rate limits

💡 **Tip 2**: Use the speed control to listen at comfortable pace

💡 **Tip 3**: Download videos for offline use

💡 **Tip 4**: Batch process multiple chapters with a Python script

💡 **Tip 5**: Cache generated content to avoid regenerating

---

**You're all set! Happy learning! 🎓**

Need help? Check `SETUP_GUIDE.md` for detailed documentation.
