"""Manim scene for a single derivation step.

Rendered once per step by generate.py via the `manim` CLI. The step's
LaTeX + target duration are passed in through a JSON file pointed to by the
STEP_SPEC env var, so this file stays generic and reusable across steps.
"""

import json
import os

from manim import BLACK, WHITE, MathTex, Scene, Write


class StepScene(Scene):
    def construct(self):
        # White background, dark text (Khan Academy style)
        self.camera.background_color = WHITE

        with open(os.environ["STEP_SPEC"]) as f:
            spec = json.load(f)

        latex = spec["latex"]
        duration = float(spec.get("duration", 3.0))

        try:
            formula = MathTex(latex, color=BLACK)
        except Exception:
            # If LaTeX fails to compile, fall back to showing it as plain text
            from manim import Text
            formula = Text(latex, color=BLACK)

        formula.scale(1.3)

        write_time = min(1.5, max(0.5, duration * 0.4))
        self.play(Write(formula), run_time=write_time)
        self.wait(max(0.1, duration - write_time))
