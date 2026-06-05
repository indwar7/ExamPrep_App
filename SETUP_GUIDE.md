# AI Content Platform - Setup Guide

Complete platform for generating educational content with AI videos and audiobooks.

## 🚀 Quick Start

### 1. Get ElevenLabs API Key
- Visit: https://elevenlabs.io
- Sign up for free account
- Go to Settings → API Keys
- Copy your API key

### 2. Run Backend Server

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key and run server
export ELEVENLABS_API_KEY="your_api_key_here"
python run_server.py
```

Server runs on `http://localhost:5000`

### 3. Open Frontend

Open `ai-content-platform.html` in your browser:
```bash
# On macOS
open ai-content-platform.html

# On Linux
xdg-open ai-content-platform.html

# Or just double-click the file
```

### 4. Configure API Key in UI

1. Click "Configure API" button in top right
2. Paste your ElevenLabs API key
3. Click "Save Configuration"

## 📊 Features

### Video Generation
- **AI Experiment Videos**: Automatically generates videos for experiments mentioned in chapters
- **Step-by-step Demonstrations**: Each experiment broken into clear steps
- **Multiple Video Chunks**: Long content split into manageable video segments
- **Format**: MP4, ready to embed

### Audio Generation
- **Audiobook Narration**: Text-to-speech with natural Indian English voice
- **Speed Control**: Play at 0.75x to 2x speed
- **Streaming Support**: Stream or download audio files
- **Professional Quality**: Using ElevenLabs advanced models

### Content Formats
1. **Detailed Document** (PDF/Word)
   - Full chapter explanation
   - Key concepts highlighted
   - Examples and definitions
   - ~2000-3000 words

2. **Summary Notes**
   - Quick reference bullet points
   - Important definitions
   - Key terms glossary
   - ~500-700 words

3. **Illustrations Guide**
   - Concept maps
   - Process diagrams
   - Experiment setups
   - Comparison charts

4. **Full Content**
   - Complete chapter text
   - Well-structured sections
   - Download as PDF or Word Doc

## 🔧 Configuration

### Custom Voices
Default voice: "21m00Tcm4TlvDq8ikWAM" (Rachel - Female)

Other ElevenLabs voices:
- "EXAVITQu4vr4xnSDxMaL" (Bella)
- "ThT5KcBeYPX3keUQqHPh" (Antoni)
- "TxGEqnHWrfWFTfGW9XjX" (Elli)

Change in API modal or modify `content_generator.py`

### Content Customization
Edit `content_generator.py`:
- `_generate_detailed_doc()` - Document structure
- `_generate_summary_notes()` - Notes format
- `_generate_illustrations_guide()` - Illustration definitions

## 📝 Content Requirements

### Text Formatting
- NO em-dashes (—) or double hyphens (--)
- NO complex special characters
- Use simple, clear language
- Proper sentence structure

### NCERT Integration
1. Extract chapter text from NCERT PDF
2. Paste into chapter_text field
3. Platform will automatically:
   - Clean formatting
   - Generate videos
   - Create audiobook
   - Split into formats

## 🎯 Workflow

```
1. Select Class & Subject
   ↓
2. Choose Chapter
   ↓
3. Click "Generate Content"
   ↓
4. [Backend]
   ├─ Videos: Extract experiments → Generate AI videos
   ├─ Audio: Clean text → TTS narration
   ├─ Notes: Extract key points → Format as bullets
   └─ Doc: Full content → Structured document
   ↓
5. View in Tabs
   ├─ Videos: Watch experiment demonstrations
   ├─ Audio: Listen to audiobook
   ├─ Notes: Quick summary
   └─ Content: Full chapter text
   ↓
6. Download or Share
```

## 🔐 Security

- API keys stored in browser localStorage
- Never sent to unsecured servers
- Use HTTPS in production
- Add authentication layer for multi-user setup

## 🛠️ Troubleshooting

### "No videos generated"
- Check ElevenLabs API key is valid
- Ensure chapter text contains clear experiment descriptions
- Check browser console for errors (F12)

### "Audio not playing"
- Verify API key is set
- Check audio file is being generated
- Try different browser (Chrome/Firefox recommended)

### "Slow generation"
- API calls take 30-60 seconds
- Large chapters take longer
- Check internet connection
- Monitor token usage in ElevenLabs dashboard

## 📚 Chapter Structure

System expects chapters with:
- Clear headings and sections
- Numbered lists for steps
- Paragraph breaks
- Experiment descriptions

Example structure:
```
Chapter Name
============

Key Concept 1
- Point 1
- Point 2

Experiment 1: Name
1. Step one
2. Step two
3. Step three

Key Concept 2
- Point 1
- Point 2
```

## 🚀 Production Deployment

### Option 1: Docker
```bash
docker build -t edumod-ai .
docker run -e ELEVENLABS_API_KEY="key" -p 5000:5000 edumod-ai
```

### Option 2: Cloud (Vercel/Heroku)
```bash
# Deploy frontend to Vercel
vercel

# Deploy backend to Heroku
heroku create
git push heroku main
```

### Option 3: Self-hosted
```bash
# Using Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 💡 Tips & Tricks

1. **Bulk Generation**: Loop through chapters programmatically
2. **Quality Control**: Always review audio before publishing
3. **Caching**: Cache videos to avoid regenerating
4. **Analytics**: Track which chapters are accessed most
5. **Feedback**: Collect student feedback on audiobook speed

## 📞 Support

- ElevenLabs Docs: https://elevenlabs.io/docs
- API Status: https://api.elevenlabs.io/health
- Email: support@elevenlabs.io

## 📄 License

This project uses ElevenLabs API. Ensure compliance with their terms of service.

---

**Version**: 1.0
**Last Updated**: 2026-06-05
**Status**: Production Ready with API Integration
