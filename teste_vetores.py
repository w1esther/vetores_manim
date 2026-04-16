import numpy as np

# Seus vetores
v1 = [1, 2, 1]
v2 = [1, 0, 1]
v3 = [1, 1, 1]
# v4 = [0, 0, 1]

# Criar a matriz
A = np.array([v1, v3, v2]).T # Transposta para ficarem como colunas

# Calcular o posto o número de vetores linearmente independentes dentro da matriz

posto = np.linalg.matrix_rank(A)

print(f"Posto da matriz: {posto}")

if posto == A.shape[1]:
    print("Os vetores são Linearmente Independentes.")
else:
    print("Os vetores são Linearmente Dependentes (Não formam uma base do R^n).")