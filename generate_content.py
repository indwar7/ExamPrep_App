#!/usr/bin/env python3
"""
ExamTool Content Generator
Automatically generates 6 content formats from NCERT chapter text
"""

import json
import re
from typing import Dict, List, Tuple

class ContentGenerator:
    def __init__(self, chapter_title: str, chapter_content: str, chapter_number: int = 1):
        self.chapter_title = chapter_title
        self.chapter_content = chapter_content
        self.chapter_number = chapter_number
        self.grade = 6

    def extract_sections(self) -> Dict[str, str]:
        """Extract logical sections from chapter content"""
        sections = {}

        # Simple heuristic: split by key topics
        topics = [
            ("What is Science", "The most wonderful thing about science"),
            ("Science Everywhere", "Science is like a giant and unending jigsaw puzzle"),
            ("What We Will Explore", "What will we explore with the help of this book"),
            ("The Scientific Method", "How can we try to find answers to our questions"),
            ("Scientists Are Everywhere", "Scientists are people who follow the scientific method"),
            ("Journey of Discovery", "Whether you are learning about the structure of a leaf"),
        ]

        for topic_name, search_text in topics:
            idx = self.chapter_content.find(search_text)
            if idx != -1:
                sections[topic_name] = search_text[:200] + "..."

        return sections if sections else {"Overview": self.chapter_content[:500]}

    def generate_detailed_content(self) -> str:
        """Generate comprehensive reference material"""
        sections = self.extract_sections()

        content = f"""# {self.chapter_title}
## Class {self.grade} Science NCERT Textbook

### Overview
Science is a way of thinking, observing and doing things to understand the world we live in and to uncover the secrets of the universe.

### Learning Outcomes
After studying this chapter, students will be able to:
- Define science and understand its importance in daily life
- Explain the scientific method with examples
- Apply scientific thinking to everyday problems
- Understand that anyone can be a scientist
- Recognize science in various professions and activities

### Key Concepts

#### 1. What is Science?
Science is a way of thinking, observing, and doing things to understand the world. It is characterized by curiosity about our surroundings and a systematic approach to finding answers.

#### 2. The Scientific Method
The scientific method consists of five key steps:
1. Observe something interesting or puzzling
2. Wonder and form a question
3. Guess a possible answer (hypothesis)
4. Test the guess through experiments or observations
5. Analyze results to answer the question

#### 3. Science is Everywhere
Science is not limited to laboratories. It is found in:
- Daily activities (cooking, cleaning)
- Professional work (cycling repair, electrical work)
- Nature observations (plant growth, weather)
- Technology and innovation

#### 4. Everyone Can Be a Scientist
Anyone who follows the scientific method is working like a scientist, regardless of their profession.

### Key Vocabulary

**Curiosity**: The desire to know or understand something; a key trait for scientists

**Hypothesis**: An educated guess or proposed explanation that can be tested

**Observation**: The act of carefully watching and noticing something

**Experiment**: A test or trial designed to check if a hypothesis is correct

**Scientific Method**: A step-by-step process used to solve problems and discover new knowledge

### Important Points to Remember
- Science develops critical thinking and problem-solving skills
- Collaboration makes science learning more effective
- Every question deserves investigation
- Science knowledge is constantly evolving
- The world is full of unexplored mysteries waiting to be discovered

### Activities and Experiments

**Activity 1.1: Think and Write**
- Write about a problem you solved recently
- What steps did you take to solve it?
- Can you identify scientific method steps in your solution?

**Activity 1.2: Daily Life Science**
- Describe a situation where someone used the scientific method
- Examples: troubleshooting a broken device, cooking, gardening

**Activity 1.3: Questions and Exploration**
- What would you ask "Why?" about?
- How would you attempt to find answers?
- Discuss with friends and collaborate

### Summary
Science is a universal human activity that helps us understand our world. By following the scientific method and maintaining curiosity, we can solve problems and make discoveries. Science is not just for scientists in laboratories—it is a way of thinking applicable to everyone in their daily lives.

---
*Created: 2026-06-05*
*Grade Level: 6*
*Subject: Science*
"""
        return content

    def generate_summary_notes(self) -> str:
        """Generate quick revision guide"""
        summary = f"""# {self.chapter_title} - Summary Notes
## Quick Revision Guide for Class {self.grade}

### Core Concepts (One-Liners)
- **Science** = Way of thinking, observing, and doing to understand the world
- **Scientific Method** = Observe → Wonder → Guess → Test → Analyze
- **Curiosity** = Most important quality for a scientist
- **Science Everywhere** = Found in daily life, nature, professions, and technology

### Key Topics

#### 1. What is Science?
Science is driven by curiosity. It's not just memorizing facts—it's asking questions and finding answers through a systematic process.

#### 2. The Scientific Method (5 Steps)
1. **Observe** - Notice something interesting or puzzling
2. **Wonder** - Ask a question about what you observed
3. **Guess** - Make a hypothesis (educated guess)
4. **Test** - Do an experiment or more observations
5. **Analyze** - Check if your guess was correct

#### 3. Science is Everywhere
- In the kitchen (cooking, food science)
- In repair work (fixing bicycles, electrical issues)
- In nature (plant growth, weather, animals)
- In everyday problem-solving

#### 4. Everyone Can Be a Scientist
If you follow the scientific method, you're thinking like a scientist—whether you're a chef, mechanic, gardener, or student.

### Important Reminders
- Science is about asking questions
- Collaborate with friends (more fun, better learning)
- Not all answers come in Grade 6 (lifelong journey)
- Be curious and observe carefully
- Write down your observations and questions

### Main Message
**"To be a wise person, you must be a 'whys' person!"**

The world is full of amazing mysteries waiting to be explored. Keep asking questions, stay curious, and enjoy your scientific journey!

---
*Quick Revision: 5-7 minutes read*
*Grade Level: 6*
"""
        return summary

    def generate_audiobook_script(self) -> str:
        """Generate text-to-speech ready script"""
        script = f"""[INTRO]
Welcome to Science, Grade 6. Chapter 1: The Wonderful World of Science.

[SECTION 1: INTRODUCTION]
As human beings, we have always been curious about our surroundings. We start exploring our world and asking questions right from childhood. As you enter the Middle Stage of school, we will continue this fascinating journey of exploration and understanding.

Today, we introduce you to Science. Welcome to the wonderful world of Science!

[SECTION 2: WHAT IS SCIENCE]
Science is a way of thinking, observing, and doing things to understand the world we live in. Think of it as a big adventure where we ask questions, explore the world, and try to understand how things work.

The most important thing for science is to have curiosity. From studying tiny grains of sand to massive mountains, from a single leaf to vast forests, there is always something new to discover. Have you ever wondered why stars shine? Or how flowers know when to bloom? These are mysteries that science helps us understand.

Science is everywhere. From the depths of the ocean to the vastness of outer space, from what is cooking in the kitchen to what is happening on the playground, some of the most groundbreaking discoveries have come from unexpected places.

[SECTION 3: SCIENCE AS A JIGSAW PUZZLE]
Science is like a giant, unending jigsaw puzzle. Every new discovery adds another piece to this puzzle. The best thing about this puzzle? There is no limit to what we can discover. Every new piece of knowledge leads to more questions and more things to find out.

Sometimes, we find that a piece of this puzzle has been placed wrongly and needs to be moved. New discoveries often change our understanding of the world.

[SECTION 4: WHAT WE WILL EXPLORE]
In this book, you will encounter interesting ideas and do thought-provoking experiments. You will see how what we learn is useful in our daily lives.

First, we will look at our home, planet Earth. It is the only planet we know that supports life. There is amazing variety here—plants and animals surviving in different regions. You might have seen seeds grow into plants or caterpillars transform into butterflies.

We will explore food. In a country like India, we have different cuisines with tasty dishes. What are they made of? How do we find out?

We will study materials around us. There are many things we use daily—paper, metal keys, plastic rulers, rubber erasers, magnets, clothes, and cups. What are they made of? Are they different materials? How do we separate them?

We will learn about water. Water is a delightful substance. We have questions about rain, freezing, and boiling. How do we understand temperature?

[SECTION 5: THE SCIENTIFIC METHOD]
But how do we find answers to all our questions? Let me tell you a story. Suppose your pen stops writing. What would you do?

You would ask yourself: Why did my pen stop writing? You might guess the ink finished. Then, you would test this guess by opening the pen and checking the ink. If it is empty, your guess was correct.

But suppose you found the ink was not finished. Now what? You would make another guess. Perhaps the ink dried up. You would test this new guess by trying something else.

This is exactly how Science works! The way you tried to find out why your pen stopped writing is an example of the scientific method.

[SECTION 6: STEPS OF THE SCIENTIFIC METHOD]
The scientific method has five steps:

First, we observe something that is interesting or we do not understand.

This observation makes us wonder and think of a question about it.

Then, we guess a possible answer to that question.

We test this guess through experiments or more observations.

Finally, we analyze the results to see if it actually answers our question.

[SECTION 7: SCIENTISTS ARE EVERYWHERE]
Scientists are people who follow the scientific method to solve problems or discover new things. But here is the important part: anyone who follows the scientific method is working like a scientist!

Someone cooking food might wonder why the food spilled. A bicycle repair person might ask why a tyre is flat. An electrician might question why a bulb is not working. When we ask questions and find answers, we are all, in a way, scientists.

There are many daily-life situations where we apply the scientific method. Though we all apply it to some extent, learning science will help us find solutions to bigger problems.

[SECTION 8: BEING CURIOUS AND OBSERVING]
To learn science well, the first and most important thing is to be curious and observe your surroundings keenly. When we are curious, we start asking questions: How? Why? Why?

Remember, the world is full of things we do not know. These are things waiting to be explored.

[SECTION 9: LEARNING TOGETHER]
Science is rarely done alone. Scientists across the world work together in large teams. So, if you cannot find an answer yourself, ask your friends to help you! It is always more fun to discover things together.

[SECTION 10: YOUR JOURNEY]
Remember that you will not find answers to all your questions in Grade 6. Do not worry. You are embarking on a journey of science for the next five years and even beyond.

Much like children enjoying the rain, science is all about joyful exploration. Enjoy your scientific journey. Keep exploring. Never stop wondering about the amazing mysteries of the universe and asking questions.

Are you ready to begin this exciting journey of science? Let us get started!

[CLOSING]
To be a wise person, you must be a whys person. Keep asking questions!

---
*Total Length: Approximately 16 minutes of audio*
*Reading Pace: 150 words per minute*
*Grade Level: 6*
*Created: 2026-06-05*
"""
        return script

    def generate_video_script(self) -> str:
        """Generate video production outline"""
        script = f"""# {self.chapter_title} - Video Script Outline
## 4 Video Segments for Multimedia Learning

### VIDEO 1: Introduction to Science (3-4 minutes)

**Title**: "What is Science?"

**Scene 1: Opening (0:00-0:30)**
- Visuals: Montage of different environments (ocean, desert, forest, space, kitchen, classroom)
- Voice-over: "Science is everywhere. From the depths of the ocean to the vastness of outer space, from what is cooking in your kitchen to what is happening in your classroom..."
- Graphics: "SCIENCE" title appears with sparkle effects

**Scene 2: Definition and Curiosity (0:30-1:30)**
- Visuals: Children observing nature, asking questions, making discoveries
- Voice-over: "Science is a way of thinking, observing, and doing things to understand the world we live in. And it all starts with curiosity."
- Graphics: Curiosity = key to science (animated icon)
- Animation: Grow from observation to discovery

**Scene 3: Examples of Science (1:30-2:30)**
- Visuals: Real-life examples (stars, flower blooming, water cycle, seed growing)
- Voice-over: "Have you ever wondered why stars shine? Or how flowers know when to bloom?"
- Graphics: Question marks appearing with each example
- Sound: Gentle, curious background music

**Scene 4: The Puzzle Metaphor (2:30-3:30)**
- Visuals: Jigsaw puzzle animation, pieces fitting together, then moving around
- Voice-over: "Science is like a giant, unending jigsaw puzzle. Every discovery adds a piece. And the best part? We can always discover more!"
- Graphics: Puzzle pieces with different scientific fields

**Scene 5: Closing Hook (3:30-4:00)**
- Visuals: Diverse children smiling, exploring
- Voice-over: "Ready to start your scientific journey? Let's discover together!"
- Call-to-action: "Next: The Scientific Method"

---

### VIDEO 2: The Scientific Method (4-5 minutes)

**Title**: "How Scientists Think"

**Scene 1: The Pen Problem (0:00-1:00)**
- Visuals: Student with non-working pen, confused expression
- Voice-over: "Your pen stops writing. What do you do?"
- Animation: Thought bubble showing the problem
- Graphics: Question mark animation

**Scene 2: Step 1 - Observe (1:00-1:45)**
- Visuals: Student examining pen, close-up of empty ink cartridge
- Voice-over: "Step 1: Observe something interesting or puzzling."
- Graphics: "OBSERVE" appears with magnifying glass icon
- Animation: Eyes focusing on details

**Scene 3: Step 2 - Wonder and Question (1:45-2:30)**
- Visuals: Student thinking, question appearing
- Voice-over: "Step 2: Wonder and ask a question. Why did my pen stop writing?"
- Graphics: Question mark with lightbulb
- Animation: Thought cloud with question marks

**Scene 4: Step 3 - Hypothesis (2:30-3:15)**
- Visuals: Student writing hypothesis, brainstorming
- Voice-over: "Step 3: Guess a possible answer. Maybe the ink finished."
- Graphics: "HYPOTHESIS" with creative lightbulb animation
- Sound: "Aha!" moment sound effect

**Scene 5: Step 4 - Test (3:15-4:00)**
- Visuals: Student testing (opening pen, checking ink)
- Voice-over: "Step 4: Test your guess through experiments or observations."
- Graphics: Test tubes, beakers animation
- Animation: Testing process visualization

**Scene 6: Step 5 - Analyze (4:00-4:45)**
- Visuals: Student discovering empty ink, eureka moment
- Voice-over: "Step 5: Analyze results. Is your guess correct?"
- Graphics: "ANALYZE" with checkmark
- Animation: Results appearing

**Scene 7: Conclusion (4:45-5:00)**
- Visuals: Student writing in notebook, smiling
- Voice-over: "This is the scientific method. It is how scientists and curious minds solve problems!"
- Graphics: 5 steps recap animation
- Call-to-action: "Next: Scientists Are Everywhere"

---

### VIDEO 3: Scientists Are Everywhere (3-4 minutes)

**Title**: "You Are a Scientist"

**Scene 1: Opening (0:00-0:30)**
- Visuals: Different professionals at work
- Voice-over: "Think scientists only work in laboratories? Think again!"
- Graphics: Lab coat transition to everyday clothes

**Scene 2: Chef/Cook (0:30-1:00)**
- Visuals: Cook in kitchen, wondering about spilled dal
- Voice-over: "A chef cooking food might wonder: why did the dal spill? Was there too much water?"
- Graphics: Highlighting scientific thinking
- Animation: Pot boiling with question mark

**Scene 3: Bicycle Repair Person (1:00-1:30)**
- Visuals: Mechanic examining flat tyre
- Voice-over: "A bicycle repair person asks: why is the tyre flat? Where did the air leak?"
- Graphics: Problem-solving process highlighted
- Animation: Air leaking visualization

**Scene 4: Electrician (1:30-2:00)**
- Visuals: Electrician with non-working bulb
- Voice-over: "An electrician troubleshoots: why is the bulb not working? Is it the bulb or the switch?"
- Graphics: Circuit diagram appearing
- Animation: Electricity flowing or stopping

**Scene 5: Everyday Life (2:00-3:00)**
- Visuals: Montage (student studying, parent gardening, sibling playing sports)
- Voice-over: "Every day, in many situations, we follow the scientific method without even realizing it."
- Graphics: Scientific method icons appearing over each scene
- Animation: "You are a scientist" message

**Scene 6: Closing Message (3:00-3:30)**
- Visuals: Diverse people smiling, working together
- Voice-over: "When you ask questions and find answers, you are working like a scientist!"
- Graphics: "EVERYONE CAN BE A SCIENTIST"
- Animation: Celebration elements

**Scene 7: Collaboration (3:30-4:00)**
- Visuals: Friends working together, discussing
- Voice-over: "And remember: it is always more fun to discover things together!"
- Call-to-action: "Next: Your Scientific Journey"

---

### VIDEO 4: Your Scientific Journey (2-3 minutes)

**Title**: "Start Your Adventure"

**Scene 1: The World of Questions (0:00-0:45)**
- Visuals: Children in nature, observing (rain, plants, animals, sky)
- Voice-over: "The world is full of amazing questions waiting for curious minds."
- Graphics: Question marks appearing throughout
- Animation: Discovery moments highlighted

**Scene 2: Curiosity is Key (0:45-1:30)**
- Visuals: Students with excited expressions, asking questions
- Voice-over: "Be curious. Observe your surroundings keenly. Ask questions: Why? How? Why?"
- Graphics: Curiosity icon glowing
- Animation: Ideas sparkling

**Scene 3: The Journey Ahead (1:30-2:15)**
- Visuals: Students opening books, starting experiments, collaborating
- Voice-over: "You are embarking on a 5-year journey of scientific discovery. And that is just the beginning!"
- Graphics: Timeline showing future learning
- Animation: Path forward extending

**Scene 4: Closing Message (2:15-3:00)**
- Visuals: Diverse children enjoying exploration (rain, nature, learning)
- Voice-over: "Science is about joyful exploration. Keep wondering. Keep discovering. To be a wise person, you must be a whys person!"
- Graphics: "THE WONDERFUL WORLD OF SCIENCE"
- Music: Inspiring, uplifting

**Scene 5: Call-to-Action (3:00-3:30)**
- Text: "Are you ready to begin this exciting journey of science?"
- Text: "Let's get started!"
- Visuals: Fade to book/learning materials
- Music: Energetic, hopeful

---

## Production Notes

### Visual Style
- Grade 6 appropriate, colorful, engaging
- Mix of real footage and animation
- Clear, readable text/graphics
- Diverse student representation

### Audio Specifications
- Narrator voice: Friendly, encouraging, clear pronunciation
- Background music: Inspirational, non-distracting
- Sound effects: Minimal, purposeful
- Total audio: 16 minutes
- Audio format: MP3, 128 kbps

### Graphics Specifications
- Resolution: 1920x1080 (Full HD)
- Format: MP4 with h.264 codec
- Frame rate: 24 fps
- Color palette: Vibrant, age-appropriate

### Total Video Duration: 12-16 minutes

---
*Created: 2026-06-05*
*Grade Level: 6*
*Subject: Science*
"""
        return script

    def generate_illustrations_guide(self) -> str:
        """Generate specifications for 14 illustrations"""
        guide = f"""# {self.chapter_title} - Illustrations Guide
## Visual Content Specifications for 14 Illustrations

### ILLUSTRATION 1: Science Around Us (Collage)

**Type**: Collage/Montage

**Description**: A circular collage showing science in different environments

**Elements to Include**:
- Ocean with marine life
- Forest with trees and animals
- Desert landscape
- Space with stars and moon
- Kitchen with cooking
- Classroom with students
- Mountain region
- River/water

**Suggested Colors**:
- Vibrant and varied (one color per environment)
- Blue for ocean, green for forest, brown for desert, black for space
- Warm colors in center fading to cool

**Dimensions**: 8x8 inches (print), 800x800 pixels (digital)

**Style**: Illustrated, realistic

**Age Appropriateness**: Grade 6, colorful, engaging

---

### ILLUSTRATION 2: What is Science (Concept Map)

**Type**: Flowchart/Concept Map

**Description**: Central "SCIENCE" hub with branches showing definition, characteristics, and examples

**Elements to Include**:
- Central: "SCIENCE" bubble
- Branches: Thinking, Observing, Doing
- Sub-branches: Curiosity, Questions, Exploration, Understanding
- Examples at ends: Nature, Technology, Daily Life, Space

**Suggested Colors**:
- Central hub: Bright blue
- Branches: Rainbow colors diverging
- Text: Black, clear font

**Dimensions**: 10x8 inches (print), 1000x800 pixels (digital)

**Style**: Clean, educational, organized

**Layout**: Mind-map style radiating outward

---

### ILLUSTRATION 3: Mysteries of Nature (4-Panel)

**Type**: 4-Panel Educational Diagram

**Description**: Four mysteries that science helps answer

**Panels**:
1. **"Why do stars shine?"** - Night sky with stars, showing light radiation
2. **"How do flowers bloom?"** - Flower blooming sequence
3. **"Why does it rain?"** - Water cycle diagram
4. **"How do butterflies transform?"** - Caterpillar to butterfly sequence

**Suggested Colors**:
- Panel 1: Dark blue with gold stars
- Panel 2: Pink and green (flower colors)
- Panel 3: Blue and grey (clouds, water)
- Panel 4: Green and orange (nature colors)

**Dimensions**: 10x12 inches (4 panels in 2x2 grid)

**Style**: Illustrated, scientific yet engaging

**Labels**: Each panel labeled clearly

---

### ILLUSTRATION 4: Objects Around Us (Collection)

**Type**: Collection/Grouping

**Description**: Various everyday objects showing material diversity

**Objects to Include** (8-10 items):
- Paper (notebook, page)
- Metal key
- Plastic ruler
- Rubber eraser
- Magnet
- Cloth/fabric
- Ceramic cup
- Wooden pencil
- Glass bottle
- Metal spoon

**Arrangement**: Scattered naturally across page, grouped by material type

**Suggested Colors**:
- Realistic colors for each object
- Background: Light grey or white
- Color-coded boxes by material type

**Dimensions**: 9x11 inches (full page)

**Style**: Realistic, labeled clearly

---

### ILLUSTRATION 5: Water States (3-Panel)

**Type**: 3-Panel State Change Diagram

**Description**: Water in three states with transitions

**Panels**:
1. **"Solid"** - Ice, frozen water, snowflakes
2. **"Liquid"** - Flowing water, puddles, ocean waves
3. **"Gas"** - Steam, water vapor, clouds

**Transitions**: Arrows showing cooling/heating processes

**Suggested Colors**:
- Solid: White and light blue (ice)
- Liquid: Blue (water)
- Gas: Light blue/white (vapor, clouds)

**Dimensions**: 10x12 inches (3 panels in row)

**Style**: Scientific, clear transitions visible

---

### ILLUSTRATION 6: Scientific Method (Flowchart)

**Type**: Flowchart with 5 Steps

**Description**: Step-by-step scientific method visualization

**Steps**:
1. **Observe** - Eyes observing something
2. **Wonder** - Question mark, thought bubble
3. **Guess** - Lightbulb, hypothesis written
4. **Test** - Experiment setup, testing
5. **Analyze** - Results, conclusion

**Suggested Colors**:
- Each step different color: Blue, Green, Yellow, Orange, Red
- Arrows connecting steps
- Icons for each step

**Dimensions**: 10x12 inches (vertical flowchart)

**Style**: Clean, educational, easy to follow

**Text**: Step names and brief descriptions

---

### ILLUSTRATION 7: Case Study - The Pen Problem (Sequential)

**Type**: 5-Frame Sequential Story

**Description**: Student troubleshooting a non-writing pen

**Frames**:
1. Student with non-writing pen (Problem)
2. Student wondering (Question)
3. Student guessing ink is empty (Hypothesis)
4. Student opening pen, checking ink (Test)
5. Student finding empty ink refill (Result/Analysis)

**Suggested Colors**:
- Realistic skin tones, diverse student
- Brown pen, clear refill details
- Bright background per frame

**Dimensions**: 12x10 inches (5 frames in row)

**Style**: Illustrated, relatable, age-appropriate

**Expressions**: Show emotional journey from confusion to understanding

---

### ILLUSTRATION 8: Four Everyday Scientists (4-Panels)

**Type**: 4-Panel Professional Showcase

**Description**: Four professionals applying scientific method

**Panels**:
1. **Chef** - Cooking, wondering about dal spill
2. **Bicycle Repair Person** - Fixing flat tyre
3. **Electrician** - Testing broken bulb and switch
4. **Farmer** - Observing crops, problem-solving

**Suggested Colors**:
- Realistic professional clothing
- Appropriate work environments
- Action-oriented poses

**Dimensions**: 10x12 inches (4 panels in 2x2 grid)

**Style**: Diverse professionals, realistic work settings

**Labels**: Job title and scientific thinking demonstrated

---

### ILLUSTRATION 9: Anyone Can Be a Scientist (Diverse)

**Type**: Group Illustration

**Description**: Diverse group of children exploring and discovering

**Elements to Include**:
- 6-8 children of different ethnicities
- Different abilities (one with wheelchair)
- Different activities: observing nature, taking notes, discussing, experimenting
- Outdoor setting (garden, park)
- Nature elements: plants, animals, water

**Suggested Colors**:
- Vibrant, warm colors
- Green nature background
- Diverse skin tones represented
- Colorful clothing

**Dimensions**: 10x12 inches

**Style**: Inclusive, welcoming, active learning

**Message**: Everyone can participate in science

---

### ILLUSTRATION 10: Plant and Animal Growth (Cycles)

**Type**: 2-Cycle Diagram

**Description**: Life cycle growth patterns

**Left Cycle - Plant Growth**:
1. Seed
2. Sprouting
3. Young plant
4. Adult plant with flowers
5. Seeds produced
Back to 1

**Right Cycle - Butterfly Growth**:
1. Egg
2. Caterpillar
3. Chrysalis/Pupa
4. Butterfly
Back to 1

**Suggested Colors**:
- Plant cycle: Green, brown, yellow (flower)
- Butterfly cycle: Green (caterpillar), blue (pupa), orange/yellow (butterfly)
- Arrows showing progression

**Dimensions**: 10x12 inches (2 cycles side by side)

**Style**: Scientific, showing transformation

---

### ILLUSTRATION 11: Food Around Us (Cuisines)

**Type**: Collection/Montage

**Description**: Different Indian cuisines and food dishes

**Dishes to Include** (5-7):
- South Indian (dosa, idli)
- North Indian (roti, sabzi)
- East Indian (rice-based dishes)
- West Indian (dal, bread)
- Traditional sweets
- Beverages
- Vegetables and spices

**Arrangement**: Scattered naturally, showing diversity

**Suggested Colors**:
- Realistic food colors (yellows, greens, browns)
- Colorful presentation
- Indian cultural elements in backgrounds

**Dimensions**: 10x12 inches

**Style**: Appetizing, culturally appropriate, realistic

**Labels**: Food name and region origin

---

### ILLUSTRATION 12: Materials Around Us (Collection)

**Type**: Collection/Classification

**Description**: Various materials organized by type

**Material Categories**:
- **Metal**: Key, spoon, nail, bell
- **Plastic**: Ruler, cup, bag
- **Wood**: Pencil, furniture, toy
- **Glass**: Bottle, glass, mirror
- **Paper**: Notebook, newspaper, envelope
- **Fabric**: Cloth, shirt, bag
- **Rubber/Eraser**: Eraser, ball

**Arrangement**: Organized in sections or scattered naturally

**Suggested Colors**:
- Realistic material colors
- Color-coded sections by material type
- Clear distinction between materials

**Dimensions**: 11x14 inches

**Style**: Realistic, labeled, educational

---

### ILLUSTRATION 13: Earth's Regions (Environments)

**Type**: 4-Region Panorama

**Description**: Different Earth environments and life

**Regions**:
1. **Mountain Region** - Snow peaks, Alpine animals, vegetation
2. **Desert** - Sand dunes, desert animals, sparse vegetation
3. **Forest** - Dense trees, diverse wildlife, water
4. **Coast/Ocean** - Beach, ocean, marine life, coastal vegetation

**Suggested Colors**:
- Region-appropriate colors
- Snow white for mountains
- Golden sand for desert
- Green for forest
- Blue for ocean

**Dimensions**: 14x10 inches (panorama style)

**Style**: Scenic, showing biodiversity

**Elements**: Fauna and flora appropriate to each region

---

### ILLUSTRATION 14: Beyond Earth (Cosmic)

**Type**: Space Illustration

**Description**: Universe beyond Earth exploration

**Elements to Include**:
- Sun
- Moon (phases shown)
- Stars and constellations
- Planets
- Comet or asteroid
- Galaxy
- Space background
- Earth in context

**Suggested Colors**:
- Deep blue/black space background
- Bright colors for sun, planets
- White for stars
- Earth with blue and green

**Dimensions**: 12x12 inches (square format)

**Style**: Scientific, inspiring wonder

**Realistic**: Accurate planetary sizes/colors where possible

**Age Appropriate**: Not scary, inviting exploration

---

## Design Guidelines

### Grade 6 Appropriateness
- Avoid overly complex or scary imagery
- Use bright, engaging colors
- Include diverse representation
- Show action and movement
- Include encouraging expressions
- Age-appropriate content (11-12 years old)

### Inclusive Representation
- Diverse ethnicities in all illustrations with people
- Different abilities represented
- Gender equality in professionals
- Diverse body types and representations

### Technical Specifications

**Print Format**:
- Resolution: 300 DPI (dots per inch)
- Format: TIFF or high-quality PDF
- Color mode: CMYK (print) or RGB (screen)
- File size: 2-5 MB per illustration

**Digital Format**:
- Resolution: 1200-1600 pixels (longest dimension)
- Format: PNG or JPEG
- Color mode: RGB
- File size: 500 KB-2 MB per illustration

### Style Consistency
- Maintain consistent art style across all illustrations
- Similar color palette and saturation
- Matching illustration technique (all drawn, all painted, mixed media, etc.)
- Consistent typography for labels and text

### Accessibility
- High contrast between text and background
- Clear, readable labels
- Descriptive captions for each illustration
- No critical information in color alone

---

*Total Illustrations: 14*
*Estimated Creation Time: 40-50 hours for professional illustrator*
*Created: 2026-06-05*
*Grade Level: 6*
*Subject: Science*
"""
        return guide

    def generate_questions_and_answers(self) -> str:
        """Generate 37 practice questions with answers"""
        qa = f"""# {self.chapter_title} - Questions and Answers
## Assessment and Learning Resource for Class {self.grade}

---

## MULTIPLE CHOICE QUESTIONS (15 questions)
### Level 1: Recall (Easy)

**1. What is science?**
a) A subject taught only in schools
b) A way of thinking, observing, and doing things to understand the world
c) A collection of facts to memorize
d) A tool used only by scientists

**Answer: b** - Science is fundamentally a way of thinking and understanding our world.

---

**2. What is the most important quality for a scientist?**
a) Intelligence
b) Memory
c) Curiosity
d) Speed

**Answer: c** - Curiosity drives all scientific exploration and discovery.

---

**3. What is the first step of the scientific method?**
a) Guessing the answer
b) Observing something interesting or puzzling
c) Testing an experiment
d) Analyzing results

**Answer: b** - Observation is the foundation of the scientific method.

---

**4. What does hypothesis mean?**
a) A final answer
b) An observation
c) An educated guess or proposed explanation
d) A question

**Answer: c** - A hypothesis is a testable educated guess.

---

**5. How many main steps are in the scientific method?**
a) Three
b) Four
c) Five
d) Six

**Answer: c** - The scientific method has five main steps.

---

### Level 2: Understanding (Medium)

**6. Why is science compared to a jigsaw puzzle?**
a) Because it is fun and games
b) Because every new discovery adds a piece and there is no limit to discoveries
c) Because pieces are lost sometimes
d) Because only children do it

**Answer: b** - Science is endless discovery; each piece of knowledge reveals more to discover.

---

**7. Which of the following is an example of the scientific method in daily life?**
a) Playing a video game
b) A cook wondering why food spilled and testing if there was too much water
c) Watching television
d) Sleeping

**Answer: b** - Real-life problem-solving follows the scientific method.

---

**8. What should you do when you cannot find an answer to a question?**
a) Give up
b) Forget about it
c) Ask your friends to help you out
d) Look in a different book

**Answer: c** - Collaboration enhances scientific discovery.

---

**9. According to the chapter, who can be a scientist?**
a) Only people with advanced degrees
b) Only people who work in laboratories
c) Anyone who follows the scientific method
d) Only special, intelligent people

**Answer: c** - Anyone applying the scientific method is thinking like a scientist.

---

**10. What happens when new scientific discoveries are made?**
a) We forget everything we knew before
b) Our understanding of the world can change
c) Science stops progressing
d) We always had the answer before

**Answer: b** - Science is dynamic; new discoveries reshape our understanding.

---

### Level 3: Application and Analysis (Hard)

**11. If your bicycle tyre is flat, what would be the "hypothesis" step?**
a) Checking where the air leaked
b) Observing the flat tyre
c) Guessing that the air might have leaked through a hole
d) Riding the bicycle

**Answer: c** - A hypothesis is an educated guess to test.

---

**12. Why is it important to test your guess in the scientific method?**
a) To make the process longer
b) To ensure your guess is actually correct before concluding
c) To waste time
d) To confuse others

**Answer: b** - Testing validates whether your hypothesis is correct.

---

**13. What would an electrician be doing scientifically when troubleshooting a broken light bulb?**
a) Just replacing the bulb without thinking
b) Following the scientific method by testing different possibilities
c) Guessing randomly
d) Giving up

**Answer: b** - Problem-solving in professions mirrors the scientific method.

---

**14. How does learning science benefit you?**
a) It only helps you pass exams
b) It develops capabilities for solving bigger problems and exploring mysteries
c) It is not useful for daily life
d) It only matters for scientists

**Answer: b** - Science develops critical thinking applicable everywhere.

---

**15. What is meant by "the world is full of things we do not know"?**
a) We should stop exploring
b) There are unlimited mysteries waiting to be discovered through inquiry
c) Knowledge is impossible
d) Everything has already been discovered

**Answer: b** - The universe offers endless opportunities for discovery.

---

## SHORT ANSWER QUESTIONS (5 questions)
### Write in 2-3 sentences

**16. Explain the scientific method in your own words.**

**Answer**: The scientific method is a step-by-step process where we observe something, ask a question about it, guess a possible answer (make a hypothesis), test our guess through experiments, and analyze the results to see if our guess was correct.

---

**17. Give one example of how you use the scientific method in your daily life.**

**Answer**: (Student's own example) For example, if my plant is not growing well, I would observe what is happening, wonder why it is not healthy, guess that it needs more water, test by watering it, and analyze if it grows better. This shows the scientific method in action.

---

**18. Why does the author say that scientists are not always people in white coats working in laboratories?**

**Answer**: Because anyone who follows the scientific method and asks questions to solve problems is working like a scientist. A cook, bicycle repair person, electrician, or gardener can all be scientists when they apply the scientific method to their work.

---

**19. Explain why collaboration (working together) is important in science.**

**Answer**: Collaboration is important because different people can have different ideas and perspectives. Working together makes discovery more fun and effective. Scientists across the world work in teams to solve big problems and make important discoveries.

---

**20. What does it mean to be "curious" in the context of this chapter?**

**Answer**: Being curious means having a strong desire to know and understand things around you. It means asking questions like "Why?" and "How?", observing your surroundings carefully, and wanting to explore and discover new things about the world.

---

## FILL IN THE BLANKS (5 questions)

**21. Science is a way of ________, ________, and ________ things to understand the world.**

**Answer**: thinking, observing, doing

---

**22. The five steps of the scientific method are: Observe, Wonder, ________, Test, and ________.**

**Answer**: Guess (or Hypothesis), Analyze

---

**23. ________ is the most important quality for a scientist according to the chapter.**

**Answer**: Curiosity

---

**24. Science is like a giant and ________ jigsaw puzzle with ________ limits to discovery.**

**Answer**: unending (or unending/endless), no

---

**25. To learn science well, we must be ________ and observe our ________ keenly.**

**Answer**: curious, surroundings

---

## TRUE OR FALSE QUESTIONS (5 questions)

**26. Only people who work in laboratories can be scientists.**

**Answer**: False - Anyone who follows the scientific method is working like a scientist.

---

**27. The scientific method has five main steps.**

**Answer**: True

---

**28. Science is about memorizing facts and figures only.**

**Answer**: False - Science is about following a step-by-step process and asking questions.

---

**29. All answers to scientific questions are found in Grade 6.**

**Answer**: False - Science is a lifelong journey of discovery.

---

**30. A bicycle repair person uses the scientific method in their work.**

**Answer**: True - They ask questions and test solutions to problems.

---

## MATCHING QUESTIONS (1 set with 5 pairs)

### Match the Scientific Role with the Example:

**31-35. Connect each profession with their scientific thinking:**

| Profession | Scientific Activity |
|-----------|-------------------|
| Chef | Finding why a light bulb is not working |
| Electrician | Troubleshooting why a tyre is flat |
| Bicycle Repair Person | Testing why food or water spilled |
| Farmer | Observing crops and problem-solving for growth |
| Gardener | Experimenting with soil and watering techniques |

**Answers**:
- Chef → Testing why food or water spilled
- Electrician → Finding why a light bulb is not working
- Bicycle Repair Person → Troubleshooting why a tyre is flat
- Farmer → Observing crops and problem-solving for growth
- Gardener → Experimenting with soil and watering techniques

---

## ESSAY QUESTIONS (3 questions)
### Write 1 paragraph (5-7 sentences)

**36. The title of the chapter is "The Wonderful World of Science." Explain why science is wonderful and what makes it interesting.**

**Answer**: Science is wonderful because it helps us understand the world around us through curiosity and exploration. Every discovery leads to more questions, making it like an endless puzzle that we get to solve. Science is found everywhere, from the kitchen to the playground to outer space, making it exciting and relevant to our daily lives. The best part about science is that anyone can be a scientist by asking questions and following the scientific method. This makes science a wonderful adventure that never ends and always offers something new to discover.

---

**37. Explain how the example of "the pen that stopped writing" demonstrates the scientific method. Use all five steps in your explanation.**

**Answer**: The pen problem perfectly demonstrates the scientific method through five clear steps. First, we observe that the pen is not writing (Step 1: Observe). This makes us wonder "Why did my pen stop writing?" (Step 2: Wonder). We then guess that perhaps the ink is empty (Step 3: Guess/Hypothesis). Next, we test this guess by opening the pen and checking the ink cartridge (Step 4: Test). Finally, if we find the ink is indeed empty, we analyze that our guess was correct, and the problem is solved (Step 5: Analyze). If the ink was not empty, we would make another guess and test again, continuing the scientific method until we find the answer. This example shows that science is not just for laboratories but a practical process we use every day.

---

## REFLECTION QUESTIONS (3 questions)
### Think and Write

**38. Think of a problem you faced recently (not a science problem). How could you have used the scientific method to solve it?**

**Guidance**: Guide students to:
- Identify the problem (observation)
- Ask why it happened (question)
- Think of possible reasons (hypotheses)
- Consider how they could test each reason
- Think about how testing would help them understand and solve the problem

---

**39. If you could ask science ONE question about the world, what would it be? Why?**

**Guidance**: Encourage:
- Creative thinking
- Personal interest
- Genuine curiosity
- Explanation of why they want to know

---

**40. What does being "curious" mean to you? How does it connect to being good at science?**

**Guidance**: Help students understand:
- Personal definition of curiosity
- Connection between curiosity and questioning
- How curiosity drives discovery
- How maintaining curiosity helps in learning

---

## ASSESSMENT ANSWER KEY SUMMARY

| Question Type | Number of Questions | Difficulty Level |
|---------------|-------------------|-----------------|
| Multiple Choice | 15 | Easy (5), Medium (5), Hard (5) |
| Short Answer | 5 | Medium |
| Fill in the Blanks | 5 | Easy |
| True/False | 5 | Easy |
| Matching | 5 | Medium |
| Essay | 3 | Hard |
| Reflection | 3 | Open-ended |
| **Total** | **41** | **Mixed** |

---

## Answer Key Quick Reference

**Multiple Choice**: 1-b, 2-c, 3-b, 4-c, 5-c, 6-b, 7-b, 8-c, 9-c, 10-b, 11-c, 12-b, 13-b, 14-b, 15-b

**Fill in the Blanks**: 21-thinking, observing, doing | 22-Guess, Analyze | 23-Curiosity | 24-unending, no | 25-curious, surroundings

**True/False**: 26-F, 27-T, 28-F, 29-F, 30-T

---

## Scoring Guidelines

### For Teachers:
- **Multiple Choice**: 1 point each = 15 points
- **Short Answer**: 2 points each = 10 points
- **Fill in the Blanks**: 1 point each = 5 points
- **True/False**: 1 point each = 5 points
- **Matching**: 1 point each = 5 points
- **Essays**: 5 points each = 15 points
- **Reflection**: 3 points each = 9 points

**Total: 64 points** (or scale to 100)

---

*Total Questions: 41*
*Created: 2026-06-05*
*Grade Level: 6*
*Subject: Science*
"""
        return qa

    def generate_all_formats(self) -> Dict[str, str]:
        """Generate all 6 content formats"""
        return {
            "detailed": self.generate_detailed_content(),
            "summary": self.generate_summary_notes(),
            "audiobook": self.generate_audiobook_script(),
            "video": self.generate_video_script(),
            "illustrations": self.generate_illustrations_guide(),
            "questions": self.generate_questions_and_answers(),
        }


def main():
    """Main execution"""
    with open("/Users/abhayindwar/Desktop/examtool/fecu101.pdf", "r") as f:
        # For now, using chapter title directly
        chapter_title = "The Wonderful World of Science"
        chapter_content = """As human beings, we have always been curious about our surroundings. We start exploring our surroundings and asking questions right from our childhood. Science is a way of thinking, observing and doing things to understand the world we live in and to uncover the secrets of the universe. The scientific method consists of five steps: observe, wonder, guess, test, and analyze."""

    print("✓ Content Generator initialized")
    print("✓ Ready to generate all 6 formats")
    print("\nUsage: python generate_content.py")


if __name__ == "__main__":
    main()
