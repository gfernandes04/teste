#faça um codigo rm python que multiplique uma matriz 3x3 por um vetor 3x1
import numpy as np
# Definindo a matriz 3x3
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Definindo o vetor 3x1
vetor = np.array([[1],
                  [2],
                  [3]])

# Multiplicando a matriz por o vetor
resultado = np.dot(matriz, vetor)

# Imprimindo o resultado
print(resultado)
