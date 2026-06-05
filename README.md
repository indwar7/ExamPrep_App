# NCERT Science Grade 6 - Complete Learning Platform

A professional, interactive educational platform for NCERT Science Grade 6 with video explanations, experiments, and interactive quizzes.

## Features

### 1. Landing Page (intro-science.html)
- Beautiful hero section with animated effects
- Learning journey timeline
- Feature cards and statistics
- Call-to-action button to start learning

### 2. Main Learning Platform (phase4-interactive-app.html)

#### Lesson Tab
- Professional lesson content with progress tracking
- Progress bar shows scrolling completion
- Learning progress indicator (5 stages)
- Scientific method flowchart
- 4 branches of science with professional icons
- Visual summary section
- No emojis - clean, professional design

#### Experiments Tab
- 8 hands-on science experiments
- Colorful visual guides for each experiment
- Step-by-step procedures
- Real-world connections
- Visual diagrams and charts

#### Quiz Tab
- 5 interactive multiple-choice questions
- 10-second video explanations for each answer
- Score tracking
- White background educational videos

## Quick Start

### Local Testing
```bash
cd /Users/abhayindwar/Desktop/examtool
python3 -m http.server 8000
# Visit http://localhost:8000/intro-science.html
```

## Deployment on Vercel

### Requirements
- GitHub account
- Vercel account (vercel.com)

### Step 1: Initialize Git Repository
```bash
cd /Users/abhayindwar/Desktop/examtool
git init
git add .
git commit -m "NCERT Science Platform - Initial commit"
```

### Step 2: Create GitHub Repository
1. Go to https://github.com/new
2. Create a new repository named "examtool"
3. Follow instructions to push your local code:
```bash
git remote add origin https://github.com/YOUR-USERNAME/examtool.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Vercel
1. Visit https://vercel.com/abhays-projects-8f26f58c
2. Click "Add New" → "Project"
3. Click "Import Git Repository"
4. Paste your GitHub repository URL
5. Click "Import"
6. Configure Project (no special settings needed)
7. Click "Deploy"

### Step 4: Access Your Site
After deployment, you'll get a URL like:
- `https://examtool-yourname.vercel.app/intro-science.html`

## Project Structure

```
examtool/
├── intro-science.html              # Landing page
├── phase4-interactive-app.html     # Main platform
├── video/                          # Video files (10 MP4 files)
├── vercel.json                     # Vercel config
├── .vercelignore                   # Files to ignore during deployment
└── README.md                       # This file
```

## Features

✅ Professional landing page with animations
✅ Progress bar (updates as user scrolls)
✅ Learning progress indicator (5 sections)
✅ Scientific method flowchart
✅ 4 science branches (Physics, Chemistry, Biology, Earth Science)
✅ 8 detailed experiments with visuals
✅ 5 interactive quiz questions
✅ 10 video explanations
✅ Responsive design
✅ Professional appearance (no emojis)
✅ Clean typography
✅ Colorful, engaging design

## Performance

- Automatic image optimization (Vercel)
- Video streaming optimized
- Static file caching enabled
- Fast CDN delivery globally

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Support

For issues or questions, check the files:
- `intro-science.html` - Landing page code
- `phase4-interactive-app.html` - Main platform code

---

**Created for NCERT Science Grade 6 students**
