#!/usr/bin/env python3
"""
Batch Content Generation Script
Automates generation of content for multiple chapters
"""

import os
import json
import time
from content_generator import ContentGenerator, ContentRequest
from dotenv import load_dotenv

load_dotenv()

class BatchProcessor:
    """Processes multiple chapters in batch"""

    def __init__(self, api_key: str):
        self.generator = ContentGenerator(api_key)
        self.results = []
        self.errors = []

    def process_chapters(self, chapters_config: list) -> dict:
        """
        Process multiple chapters

        chapters_config format:
        [
            {
                "class": 6,
                "subject": "science",
                "chapter_name": "Food: Where Does It Come From?",
                "chapter_text": "..."
            },
            ...
        ]
        """
        print("\n" + "="*70)
        print("🚀 BATCH CONTENT GENERATION")
        print("="*70)

        total = len(chapters_config)
        print(f"\n📚 Processing {total} chapters...\n")

        for i, chapter_config in enumerate(chapters_config, 1):
            print(f"\n[{i}/{total}] Processing: {chapter_config['chapter_name']}")
            print("-" * 70)

            try:
                # Generate content
                start_time = time.time()

                request = ContentRequest(
                    class_level=chapter_config['class'],
                    subject=chapter_config['subject'],
                    chapter_name=chapter_config['chapter_name'],
                    chapter_text=chapter_config.get('chapter_text', '')
                )

                result = self.generator.generate_all_formats(request)
                elapsed = time.time() - start_time

                # Store result
                self.results.append({
                    "chapter": chapter_config['chapter_name'],
                    "status": "success",
                    "time_seconds": elapsed,
                    "formats_generated": list(result['formats'].keys())
                })

                print(f"   ✅ Success ({elapsed:.1f}s)")
                print(f"   📺 Videos: {len(result['formats']['videos']['videos'])} chunks")
                print(f"   🎧 Audiobook: {result['formats']['audiobook'].get('estimated_duration_seconds', 0):.0f}s")
                print(f"   📝 Summary: {result['formats']['summary_notes']['word_count']} words")

            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
                self.errors.append({
                    "chapter": chapter_config['chapter_name'],
                    "error": str(e)
                })

            # Rate limiting
            if i < total:
                time.sleep(2)  # 2 second delay between chapters

        return self._generate_report()

    def _generate_report(self) -> dict:
        """Generate processing report"""
        return {
            "total_chapters": len(self.results) + len(self.errors),
            "successful": len(self.results),
            "failed": len(self.errors),
            "results": self.results,
            "errors": self.errors
        }

    def save_report(self, filename: str = "batch_report.json"):
        """Save report to file"""
        report = self._generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n📊 Report saved to: {filename}")
        return report


# Sample NCERT Chapters for Class 6 Science
CLASS_6_SCIENCE_CHAPTERS = [
    {
        "class": 6,
        "subject": "science",
        "chapter_name": "Food: Where Does It Come From?",
        "chapter_text": """
        Food is essential for all living organisms. It provides energy and materials for growth.
        Different organisms obtain food in different ways.

        Plants produce their own food through photosynthesis using sunlight, water, and carbon dioxide.
        This process occurs in the leaves where chlorophyll captures light energy.

        Animals cannot make their own food. They depend on plants or other animals for food.
        Some animals eat only plants (herbivores), while others eat meat (carnivores).
        Many animals eat both plants and animals (omnivores).

        Experiments:
        1. Ingredient Identification: Separate different foods and identify their components
        2. Nutrition Testing: Test for presence of carbohydrates, proteins, and fats in foods
        3. Observation of Plant Growth: Monitor how plants grow with different nutrients
        """
    },
    {
        "class": 6,
        "subject": "science",
        "chapter_name": "Components of Food",
        "chapter_text": """
        Food consists of various components that our body needs.

        The main components are:
        1. Carbohydrates: Provide energy. Found in rice, bread, sugar.
        2. Proteins: Help in growth and repair. Found in eggs, milk, beans.
        3. Fats: Provide energy and store it. Found in oil, butter, nuts.
        4. Vitamins: Prevent diseases. Found in fruits, vegetables.
        5. Minerals: Support body functions. Found in various foods.
        6. Water: Essential for all life processes.
        7. Fiber: Helps digestion. Found in vegetables and whole grains.

        Experiments:
        1. Starch Detection: Use iodine to identify starch in foods
        2. Protein Testing: Use heat to identify protein in foods
        3. Fat Testing: Use tissue paper to detect fats
        4. Vitamin C Testing: Use specific color changes to identify Vitamin C
        """
    },
    {
        "class": 6,
        "subject": "science",
        "chapter_name": "Fibre in Food",
        "chapter_text": """
        Fiber is a component of food that aids digestion.

        Types of Fiber:
        1. Soluble Fiber: Dissolves in water. Found in oats, beans, fruits.
        2. Insoluble Fiber: Does not dissolve in water. Found in vegetables, whole grains.

        Benefits of Fiber:
        - Helps in digestion
        - Prevents constipation
        - Helps maintain weight
        - Reduces risk of diseases

        Foods Rich in Fiber:
        - Vegetables: Carrots, spinach, beans
        - Fruits: Apples, oranges, bananas
        - Grains: Wheat, rice, oats

        Experiments:
        1. Plant Fiber Observation: Examine fiber in different plants under microscope
        2. Cellulose Analysis: Extract and observe plant cellulose
        3. Digestibility Test: Compare how different fibers are processed
        """
    }
]


def run_batch_generation():
    """Main batch generation function"""

    api_key = os.getenv('ELEVENLABS_API_KEY')

    if not api_key:
        print("\n❌ ERROR: ELEVENLABS_API_KEY not set")
        print("Run: export ELEVENLABS_API_KEY='your_key' && python batch_generate.py")
        return

    # Initialize processor
    processor = BatchProcessor(api_key)

    # Process chapters
    report = processor.process_chapters(CLASS_6_SCIENCE_CHAPTERS)

    # Print summary
    print("\n" + "="*70)
    print("📊 BATCH PROCESSING SUMMARY")
    print("="*70)
    print(f"✅ Successful: {report['successful']}")
    print(f"❌ Failed: {report['failed']}")
    print(f"📚 Total: {report['total_chapters']}")

    # Save report
    processor.save_report()

    # Print detailed results
    if report['results']:
        print("\n✅ Successful Chapters:")
        for result in report['results']:
            print(f"   • {result['chapter']} ({result['time_seconds']:.1f}s)")

    if report['errors']:
        print("\n❌ Failed Chapters:")
        for error in report['errors']:
            print(f"   • {error['chapter']}: {error['error']}")

    print("\n" + "="*70)


if __name__ == "__main__":
    run_batch_generation()
