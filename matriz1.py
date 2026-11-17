'''
Exemplo de iteração sobre uma matriz com índices e valores
'''

import os
import numpy as np

matriz = np.array([[3, 4, 1], 
                   [3, 1, 5]])

os.system('cls' if os.name == 'nt' else 'clear')
for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        print(f'Elemento [{i}, {j}]: {valor}')
soma = np.sum(matriz)
print(f'\nSoma dos Valores: {soma}')
media = np.mean(matriz)
print(f'Média dos Valores: {media:.2f}')

