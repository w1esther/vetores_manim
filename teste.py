from manim import *
import numpy as np

class Vetores(MovingCameraScene):

    def construct(self):

        plano = NumberPlane(
            background_line_style={'stroke_opacity': 0.4}
        )
        self.add(plano)
        self.wait(1)
        
        v1 = np.array([2, 2, 0])
        v2 = np.array([3, 0.7, 0])
        v_soma = v1 + v2
        v_subtracao = v1 - v2

        vetor_1 = Arrow(ORIGIN, v1, color=PINK, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)
        vetor_2 = Arrow(ORIGIN, v2, color=RED, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)

        vetor_soma = Arrow(ORIGIN, v_soma, color=ORANGE, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)

        v1_trans = Arrow(v2, v2 + v1, color=PINK, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)
        v2_trans = Arrow(v1, v1 + v2, color=RED, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)

        v1_trans_sub = Arrow(v2, v2 + (-v1), color=PINK, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)
        v2_trans_sub = Arrow(v1, v1 + (-v2), color=PINK, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)

        linha1 = Line(v1, v_soma, color=WHITE)
        linha2 = Line(v2, v_soma, color=WHITE)

        self.play(Create(vetor_1), Create(vetor_2))
        self.wait()

        self.play(
            TransformFromCopy(vetor_1, v1_trans),
            TransformFromCopy(vetor_2, v2_trans)
        )
        self.wait()

        self.play(Create(linha1), Create(linha2))
        self.wait()

        self.play(Create(vetor_soma), FadeOut(v1_trans, v2_trans))
        self.wait(2)

        self.play(
            TransformFromCopy(vetor_1, v1_trans_sub),
            TransformFromCopy(vetor_2, v2_trans_sub)
        )

        self.wait(2)