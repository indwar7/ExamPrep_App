#!/usr/bin/env python3
"""
Start the AI Content Platform backend server
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for API key
api_key = os.getenv('ELEVENLABS_API_KEY')
if not api_key:
    print("\n❌ ERROR: ELEVENLABS_API_KEY not set")
    print("\nTo get started:")
    print("1. Visit https://elevenlabs.io")
    print("2. Sign up and create an API key")
    print("3. Run: export ELEVENLABS_API_KEY='your_key_here'")
    print("4. Then run this script again\n")
    sys.exit(1)

print("✅ API Key found!")
print(f"   Key starts with: {api_key[:10]}...")

# Import after environment setup
from content_generator import app

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🎓 AI Content Platform - Backend Server")
    print("="*60)
    print("\n📍 Starting server...")
    print("🌐 Open browser: http://localhost:5000")
    print("📁 HTML file: ai-content-platform.html")
    print("\n💡 Tips:")
    print("   - Configure API key in UI (top right)")
    print("   - Select a chapter")
    print("   - Click 'Generate Content'")
    print("   - Watch videos & audiobooks generate")
    print("\n🔒 API Key: CONFIGURED")
    print("="*60 + "\n")

    # Run server
    try:
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            use_reloader=True
        )
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
