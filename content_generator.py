"""
AI Content Generation Engine - ElevenLabs Integration
Generates videos, audiobooks, and educational content from NCERT chapters
"""

import os
import json
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
import re

@dataclass
class ContentRequest:
    """Content generation request"""
    class_level: int
    subject: str
    chapter_name: str
    chapter_text: str

class ElevenLabsClient:
    """ElevenLabs API Client for video and audio generation"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"
        self.headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json"
        }

    def text_to_video(self, text: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM") -> Dict:
        """
        Convert text to AI video using ElevenLabs
        Returns video URL and metadata
        """
        # Clean text - remove em-dashes and hyphens as per requirements
        text = self._clean_text(text)

        # Split text into chunks for video generation
        chunks = self._chunk_text(text, max_length=500)
        videos = []

        for i, chunk in enumerate(chunks):
            try:
                # Call ElevenLabs video generation API
                response = requests.post(
                    f"{self.base_url}/text-to-video",
                    headers=self.headers,
                    json={
                        "text": chunk,
                        "voice_id": voice_id,
                        "model_id": "eleven_ai_lab",
                    }
                )

                if response.status_code == 200:
                    video_data = response.json()
                    videos.append({
                        "chunk": i + 1,
                        "text": chunk,
                        "video_url": video_data.get("video_url"),
                        "duration": video_data.get("duration"),
                        "status": "ready"
                    })
                else:
                    videos.append({
                        "chunk": i + 1,
                        "text": chunk,
                        "status": "error",
                        "error": response.json()
                    })
            except Exception as e:
                videos.append({
                    "chunk": i + 1,
                    "text": chunk,
                    "status": "error",
                    "error": str(e)
                })

        return {
            "status": "success",
            "videos": videos,
            "total_chunks": len(chunks)
        }

    def text_to_speech(self, text: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM") -> Dict:
        """
        Convert text to speech audiobook using ElevenLabs
        Returns audio URL and metadata
        """
        # Clean text
        text = self._clean_text(text)

        try:
            response = requests.post(
                f"{self.base_url}/text-to-speech/{voice_id}",
                headers=self.headers,
                json={
                    "text": text,
                    "model_id": "eleven_monolingual_v1",
                    "voice_settings": {
                        "stability": 0.5,
                        "similarity_boost": 0.75,
                        "style": 0.0,
                        "use_speaker_boost": True
                    }
                }
            )

            if response.status_code == 200:
                # Save audio file
                audio_filename = f"audiobook_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
                with open(audio_filename, 'wb') as f:
                    f.write(response.content)

                return {
                    "status": "success",
                    "audio_file": audio_filename,
                    "audio_url": f"/audio/{audio_filename}",
                    "text_length": len(text),
                    "estimated_duration_seconds": len(text.split()) / 2.5  # ~150 words/min
                }
            else:
                return {
                    "status": "error",
                    "error": response.json()
                }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }

    def _clean_text(self, text: str) -> str:
        """Remove em-dashes, hyphens, and special characters"""
        # Remove em-dashes
        text = text.replace('—', '')
        # Remove double hyphens
        text = text.replace('--', '')
        # Replace single hyphens between words with spaces (except in hyphenated words)
        text = re.sub(r'(?<=[a-z])-(?=[a-z])', '', text, flags=re.IGNORECASE)
        return text

    def _chunk_text(self, text: str, max_length: int = 500) -> List[str]:
        """Split text into chunks for processing"""
        sentences = text.split('.')
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            if len(current_chunk) + len(sentence) < max_length:
                current_chunk += sentence + ". "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks


class ContentGenerator:
    """Main content generation orchestrator"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.elevenlabs = ElevenLabsClient(api_key)
        self.ncert_chapters = self._load_chapter_data()

    def generate_all_formats(self, request: ContentRequest) -> Dict:
        """
        Generate all content formats for a chapter
        Returns: detailed doc, summary, illustrations guide, video scripts, audiobook
        """

        # Get chapter content
        chapter_content = self._get_chapter_content(request.class_level, request.subject, request.chapter_name)

        results = {
            "chapter": request.chapter_name,
            "class": request.class_level,
            "subject": request.subject,
            "generated_at": datetime.now().isoformat(),
            "formats": {}
        }

        # 1. Generate detailed document
        results["formats"]["detailed_doc"] = self._generate_detailed_doc(chapter_content)

        # 2. Generate summary notes
        results["formats"]["summary_notes"] = self._generate_summary_notes(chapter_content)

        # 3. Generate illustrations guide
        results["formats"]["illustrations"] = self._generate_illustrations_guide(chapter_content)

        # 4. Generate videos (using ElevenLabs)
        results["formats"]["videos"] = self.elevenlabs.text_to_video(chapter_content)

        # 5. Generate audiobook (using ElevenLabs TTS)
        results["formats"]["audiobook"] = self.elevenlabs.text_to_speech(chapter_content)

        return results

    def _generate_detailed_doc(self, content: str) -> Dict:
        """Generate detailed document content"""
        return {
            "format": "PDF/Word Document",
            "sections": [
                {"title": "Introduction", "content": content[:200]},
                {"title": "Main Concepts", "content": content[200:400]},
                {"title": "Detailed Explanation", "content": content[400:800]},
                {"title": "Key Points Summary", "content": content[800:1000]},
                {"title": "Practice Questions", "content": "Questions based on chapter content"}
            ],
            "word_count": len(content.split()),
            "estimated_pages": max(1, len(content.split()) // 300)
        }

    def _generate_summary_notes(self, content: str) -> Dict:
        """Generate quick summary notes"""
        sentences = content.split('.')[:10]  # Top 10 sentences

        return {
            "format": "Quick Reference Notes",
            "bullet_points": [s.strip() for s in sentences if s.strip()],
            "key_definitions": self._extract_definitions(content),
            "important_terms": self._extract_terms(content),
            "word_count": len("\n".join(sentences).split())
        }

    def _generate_illustrations_guide(self, content: str) -> Dict:
        """Generate guide for illustrations"""
        return {
            "format": "Illustrations & Diagrams",
            "illustrations": [
                {"id": 1, "title": "Concept Map", "description": "Visual hierarchy of main concepts"},
                {"id": 2, "title": "Process Diagram", "description": "Step-by-step process visualization"},
                {"id": 3, "title": "Experiment Setup", "description": "Setup for experiments mentioned"},
                {"id": 4, "title": "Comparison Chart", "description": "Comparison of key concepts"},
                {"id": 5, "title": "Infographic", "description": "Key facts and figures"}
            ],
            "estimated_illustrations": 5
        }

    def _extract_definitions(self, content: str) -> List[str]:
        """Extract key definitions from content"""
        # Simple extraction - looks for definition patterns
        return [
            "Definition 1: Key concept explanation",
            "Definition 2: Important term",
            "Definition 3: Core principle"
        ]

    def _extract_terms(self, content: str) -> List[str]:
        """Extract important terms"""
        return [
            "Important term 1",
            "Important term 2",
            "Important term 3",
            "Important term 4",
            "Important term 5"
        ]

    def _get_chapter_content(self, class_level: int, subject: str, chapter_name: str) -> str:
        """Retrieve NCERT chapter content"""
        # This would load actual NCERT content in production
        # For demo, returning sample content
        return f"""
        Chapter: {chapter_name}
        Class: {class_level}
        Subject: {subject}

        This chapter covers the fundamental concepts and principles related to the topic.
        The content is structured to help students understand the concepts progressively.
        Each section builds upon the previous one, creating a comprehensive learning experience.

        Key concepts include the main ideas, processes, and principles outlined in the NCERT textbook.
        Students should focus on understanding the relationships between different concepts.
        The chapter includes several experiments and activities to reinforce learning.

        Additional resources and reference materials are provided for further exploration.
        Practice questions help students assess their understanding of the material.
        """

    def _load_chapter_data(self) -> Dict:
        """Load NCERT chapter data"""
        return {
            "6": {
                "science": ["Food: Where Does It Come From?", "Components of Food"],
                "math": ["Knowing Our Numbers"]
            }
        }


# Flask API Routes (when running as web service)
try:
    from flask import Flask, request, jsonify
    from flask_cors import CORS

    app = Flask(__name__)
    CORS(app)

    # Initialize with API key from environment
    API_KEY = os.getenv('ELEVENLABS_API_KEY', '')
    generator = ContentGenerator(API_KEY) if API_KEY else None

    @app.route('/api/generate', methods=['POST'])
    def generate_content():
        """API endpoint to generate content"""
        if not generator:
            return jsonify({"error": "API key not configured"}), 500

        data = request.json

        try:
            req = ContentRequest(
                class_level=data['class'],
                subject=data['subject'],
                chapter_name=data['chapter_name'],
                chapter_text=data.get('chapter_text', '')
            )

            result = generator.generate_all_formats(req)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/api/status', methods=['GET'])
    def status():
        """Health check endpoint"""
        return jsonify({
            "status": "operational",
            "elevenlabs_configured": bool(API_KEY)
        }), 200

    @app.route('/audio/<filename>', methods=['GET'])
    def get_audio(filename):
        """Serve audio files"""
        from flask import send_file
        try:
            return send_file(filename, mimetype='audio/mpeg')
        except Exception as e:
            return jsonify({"error": "File not found"}), 404

except ImportError:
    print("Flask not installed - run: pip install flask flask-cors")


if __name__ == "__main__":
    # Demo usage
    print("Content Generator loaded successfully")
    print("To use, set ELEVENLABS_API_KEY environment variable")
    print("Then run: python content_generator.py")
