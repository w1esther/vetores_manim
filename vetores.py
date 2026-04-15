from manim import *
import numpy as np

class Vetores(MovingCameraScene):

    def construct(self):

        plano = NumberPlane(background_line_style=
        {'stroke_opacity': 0.4}
        )
        self.add(plano)
        self.wait(2)
        
        v1 = np.array([2, 2, 0])
        v2 = np.array([3, 0.7, 0])
        v_soma1_2 = v1 + v2

        vetor_1 = Arrow(start=ORIGIN, end=v1, color=PINK, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)

        vetor_2 = Arrow(start=ORIGIN, end=v2, color=RED, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)

        vetor_soma_1_2 =Arrow(start=ORIGIN, end=v_soma1_2, buff=0, stroke_width=2, color=ORANGE, max_tip_length_to_length_ratio=0.2)

        self.play(Create(vetor_1), Create(vetor_2),Create(vetor_soma_1_2))

        self.wait(2)