import numpy as np

def area_quadrilatero(pontos):

    if len(pontos) != 4:
        raise ValueError("Você precisa informar exatamente 4 pontos.")

    pts = np.array(pontos)

    x = pts[:, 0]
    y = pts[:, 1]

    area = 0.5 * abs(
        np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))
    )

    return area

pontos = [(0, 0), (4, 8), (8, 14), (12, 22)]

area = area_quadrilatero(pontos)
print(f"Área do quadrilátero: {area}")