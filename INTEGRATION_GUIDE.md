# 🎓 Complete Integration Guide - NCERT to AI Videos & Audiobooks

Full end-to-end guide for automating educational content creation.

---

## 📋 Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Setup Instructions](#setup-instructions)
3. [How to Use](#how-to-use)
4. [Content Integration](#content-integration)
5. [Batch Processing](#batch-processing)
6. [Customization](#customization)
7. [Deployment](#deployment)

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR WORKFLOW                             │
│                                                              │
│  1. Extract NCERT Chapter Text                              │
│     ↓                                                         │
│  2. Provide to Platform (UI or API)                          │
│     ↓                                                         │
│  3. Platform Generates Content                               │
│     ├─ Videos: Experiments visualization                     │
│     ├─ Audio: Chapter narration                              │
│     ├─ Notes: Quick summary                                  │
│     ├─ Document: Full structured content                     │
│     └─ Illustrations: Visual guides                          │
│     ↓                                                         │
│  4. Review & Publish                                         │
│     ↓                                                         │
│  5. Share with Students                                      │
└─────────────────────────────────────────────────────────────┘
```

### System Components

```
Frontend (Browser)
├── ai-content-platform.html
│   ├── Chapter Selection
│   ├── API Configuration
│   ├── Content Display
│   │   ├── Video Player
│   │   ├── Audio Player
│   │   ├── Notes
│   │   └── Document
│   └── Download Manager

Backend (Python Flask)
├── content_generator.py
│   ├── Content Processing
│   ├── ElevenLabs Integration
│   │   ├── Text-to-Video API
│   │   └── Text-to-Speech API
│   └── Content Formatting

Batch Processing
├── batch_generate.py
│   ├── Multi-chapter Processing
│   ├── Report Generation
│   └── Error Handling

Data Storage
├── Source Files
│   ├── NCERT Chapter PDFs
│   ├── Extracted Text
│   └── Metadata
├── Generated Content
│   ├── Videos (MP4)
│   ├── Audio (MP3)
│   ├── Documents (PDF/DOCX)
│   └── Notes (JSON/Markdown)
└── Configuration
    └── API Keys & Settings
```

---

## Setup Instructions

### Phase 1: Environment Setup

#### 1.1 Clone/Download Project
```bash
cd /Users/abhayindwar/Desktop/examtool
```

#### 1.2 Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 1.3 Get ElevenLabs Account
1. Visit: https://elevenlabs.io/app/sign-up
2. Create free account
3. Verify email
4. Go to: Settings → API Keys
5. Copy your API key (starts with `sk_`)

#### 1.4 Set Environment Variable
```bash
# Add to your shell profile (~/.zshrc or ~/.bash_profile)
export ELEVENLABS_API_KEY="sk_your_actual_key_here"

# Then reload
source ~/.zshrc

# Or set inline when running
ELEVENLABS_API_KEY="sk_..." python run_server.py
```

### Phase 2: Verify Setup

#### 2.1 Test Backend
```bash
python -c "from content_generator import ElevenLabsClient; print('✅ Backend OK')"
```

#### 2.2 Start Server
```bash
python run_server.py
```

You should see:
```
✅ API Key found!
🌐 Open browser: http://localhost:5000
```

#### 2.3 Open Frontend
- Open `ai-content-platform.html` in browser
- Or visit: `http://localhost:5000`

---

## How to Use

### Method 1: Web UI (Easiest)

#### Step 1: Configure API
1. Click "Configure API" (top right)
2. Paste ElevenLabs API key
3. Click "Save Configuration"

#### Step 2: Select Content
1. Choose "Class" (6, 7, 8, 9)
2. Choose "Subject" (Science, Math, English, etc.)
3. Choose "Chapter"
4. Click "Generate Content"

#### Step 3: View Results
- **🎬 Videos Tab**: Watch experiment videos
- **🎧 Audiobook Tab**: Listen to narration
- **📝 Notes Tab**: Read quick summary
- **📖 Content Tab**: View full chapter

#### Step 4: Download
- Click download buttons to get:
  - Videos (MP4)
  - Audio (MP3)
  - Documents (PDF/Word)

---

### Method 2: API (Programmatic)

#### Using Python

```python
from content_generator import ContentGenerator, ContentRequest

# Initialize
generator = ContentGenerator(api_key="sk_...")

# Create request
request = ContentRequest(
    class_level=6,
    subject="science",
    chapter_name="Food: Where Does It Come From?",
    chapter_text="Your chapter text here..."
)

# Generate
result = generator.generate_all_formats(request)

# Access results
videos = result['formats']['videos']
audiobook = result['formats']['audiobook']
notes = result['formats']['summary_notes']
document = result['formats']['detailed_doc']
```

#### Using cURL

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "class": 6,
    "subject": "science",
    "chapter_name": "Food: Where Does It Come From?",
    "chapter_text": "Your chapter text..."
  }'
```

#### Using JavaScript/Fetch

```javascript
const response = await fetch('/api/generate', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    class: 6,
    subject: 'science',
    chapter_name: 'Food: Where Does It Come From?',
    chapter_text: 'Your chapter text...'
  })
});

const result = await response.json();
console.log(result);
```

---

## Content Integration

### Extracting NCERT Content

#### Option 1: From PDF Files
```bash
# Install pdfplumber
pip install pdfplumber

# Extract text
python -c "
import pdfplumber
with pdfplumber.open('NCERT_Class6_Science.pdf') as pdf:
    for page in pdf.pages:
        print(page.extract_text())
"
```

#### Option 2: From Websites
```bash
# Install requests & beautifulsoup
pip install requests beautifulsoup4

# Scrape content
python -c "
import requests
from bs4 import BeautifulSoup
url = 'https://ncert.nic.in/...'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
print(text)
"
```

#### Option 3: Manual Entry
Simply copy-paste chapter text into the UI or Python script.

### Content Format Requirements

The platform expects content with:

```
Chapter Title
==============

Section 1: Introduction
[paragraph text]

Key Concept 1
[explanation]

Experiment Name: Description
Steps:
1. Step one
2. Step two
3. Step three
Observation: [what to observe]

Section 2: Details
[paragraph text]

Key Point: Important idea
```

### Content Cleaning

The platform automatically:
- Removes em-dashes and hyphens
- Cleans special characters
- Splits into sections
- Extracts experiments
- Identifies key concepts

---

## Batch Processing

### Single Chapter
```bash
python -c "
from batch_generate import BatchProcessor

processor = BatchProcessor(api_key='sk_...')

chapters = [{
    'class': 6,
    'subject': 'science',
    'chapter_name': 'Food: Where Does It Come From?',
    'chapter_text': 'Your content...'
}]

report = processor.process_chapters(chapters)
print(report)
"
```

### Multiple Chapters
```bash
# Pre-defined Class 6 Science chapters
python batch_generate.py
```

This generates content for:
1. Food: Where Does It Come From?
2. Components of Food
3. Fiber in Food

### Custom Batch File
Create `my_chapters.json`:
```json
[
  {
    "class": 6,
    "subject": "science",
    "chapter_name": "Chapter Name",
    "chapter_text": "Full chapter content..."
  },
  ...
]
```

Then run:
```python
import json
from batch_generate import BatchProcessor

with open('my_chapters.json') as f:
    chapters = json.load(f)

processor = BatchProcessor(api_key='sk_...')
report = processor.process_chapters(chapters)
```

---

## Customization

### Change Video Settings
Edit `content_generator.py`:

```python
def text_to_video(self, text: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM"):
    # Modify model_id for different video styles
    response = requests.post(
        f"{self.base_url}/text-to-video",
        headers=self.headers,
        json={
            "text": chunk,
            "voice_id": voice_id,
            "model_id": "eleven_ai_lab",  # Change this
        }
    )
```

### Change Voice
```python
# Different voices
voices = {
    "rachel": "21m00Tcm4TlvDq8ikWAM",  # Default
    "bella": "EXAVITQu4vr4xnSDxMaL",
    "antoni": "ThT5KcBeYPX3keUQqHPh",
    "elli": "TxGEqnHWrfWFTfGW9XjX",
}

# Use in generation
audiobook = self.elevenlabs.text_to_speech(
    text,
    voice_id=voices["bella"]
)
```

### Customize Document Format
Edit `_generate_detailed_doc()`:

```python
def _generate_detailed_doc(self, content: str) -> Dict:
    return {
        "format": "PDF/Word Document",
        "sections": [
            {"title": "Your Section", "content": "..."},
            # Add/remove sections here
        ]
    }
```

### Custom Summary Format
Edit `_generate_summary_notes()`:

```python
def _generate_summary_notes(self, content: str) -> Dict:
    return {
        "format": "Custom Format",
        "bullet_points": [...],
        "your_field": "value"
    }
```

---

## Deployment

### Option 1: Local Development
```bash
# Already set up above
python run_server.py
```

### Option 2: Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV ELEVENLABS_API_KEY=${ELEVENLABS_API_KEY}
CMD ["python", "run_server.py"]
```

Deploy:
```bash
docker build -t edumod-ai .
docker run -e ELEVENLABS_API_KEY="sk_..." -p 5000:5000 edumod-ai
```

### Option 3: Vercel (Frontend Only)
```bash
# Deploy HTML UI to Vercel
npm install -g vercel
vercel
```

Then update API endpoint in HTML:
```javascript
const apiUrl = "https://your-backend.com/api";
```

### Option 4: Heroku (Full Stack)
```bash
# Login to Heroku
heroku login

# Create app
heroku create edumod-ai

# Set API key
heroku config:set ELEVENLABS_API_KEY="sk_..."

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Option 5: AWS/GCP/Azure
Use Cloud Run, App Engine, or similar services:

```bash
# GCP Cloud Run
gcloud run deploy edumod-ai \
  --source . \
  --platform managed \
  --set-env-vars ELEVENLABS_API_KEY="sk_..."
```

---

## File Reference

```
examtool/
├── ai-content-platform.html     # Beautiful web UI
├── content_generator.py          # Core generation logic
├── batch_generate.py             # Batch processing
├── run_server.py                 # Server launcher
├── requirements.txt              # Python dependencies
├── QUICK_START.md               # 5-minute setup
├── SETUP_GUIDE.md               # Detailed setup
└── INTEGRATION_GUIDE.md          # This file
```

---

## Troubleshooting

### Issue: ImportError for flask
**Solution**:
```bash
pip install flask flask-cors
```

### Issue: API calls timeout
**Solution**:
- Check internet connection
- Verify API key is valid
- Check ElevenLabs service status
- Increase timeout in code

### Issue: Generated videos not playing
**Solution**:
- Try different browser (Chrome/Firefox)
- Check video format (should be MP4)
- Verify storage/disk space

### Issue: Audio quality issues
**Solution**:
- Check voice_id is valid
- Verify text is properly formatted
- Try with shorter text first
- Check network connection during generation

---

## Best Practices

✅ **Do:**
- Test with single chapter first
- Monitor token/credit usage in ElevenLabs
- Cache generated content
- Batch process during off-peak hours
- Keep API keys secure

❌ **Don't:**
- Share API keys in code/repositories
- Generate same content repeatedly
- Send extremely long texts
- Expose API endpoints publicly without auth
- Commit secrets to git

---

## Next Steps

1. **Try the Demo**: Run with Class 6 Science chapters
2. **Customize**: Edit content formats
3. **Batch**: Process multiple chapters
4. **Deploy**: Put online for students
5. **Monitor**: Track usage and feedback

---

## Support

- **ElevenLabs Docs**: https://elevenlabs.io/docs
- **API Limits**: Check dashboard for usage
- **Community**: Discord, GitHub issues
- **Email**: support@elevenlabs.io

---

**Version**: 1.0  
**Last Updated**: 2026-06-05  
**Status**: Production Ready
