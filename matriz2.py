'''
Matriz 2x3
'''
import os
import numpy as np

matriz = np.array([[2,4,6],
                   [3,5,7]])

def leitura():
    print("Qual a quantidade de linhas na Matriz: ",  matriz.shape[0])
    print("Qual a quantidade de colunas na Matriz: ",  matriz.shape[1])

def calculo():
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            print(f'Elemento [{l}, {c}]: {matriz[l, c]}')
    soma = np.sum(matriz)
    print(f'\nSoma dos Valores: {soma:.2f}')
    media = np.mean(matriz)
    print(f'Média dos Valores: {media:.2f}')
    maior = np.max(matriz)
    print(f'Maior Valor: {maior}')
    menor = np.min(matriz)
    print(f'Menor Valor: {menor}')

leitura()
calculo()