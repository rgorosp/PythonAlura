'''
Exemplo de iteração sobre um dicionário com chave e valor
'''

import os
import numpy as np

dicionarios = {}

def leitura():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Digite o Nome do Aluno: ")
        nome = input()
        print("Digite a Nota do Aluno: ")
        nota = float(input())
        dicionarios[nome] = nota
        print("Deseja adicionar outro aluno? (s/n)")
        resposta = input().strip().lower()
        if resposta != 's':
            imprimir()
            break

def imprimir():
    for chave, valor in dicionarios.items():
        print(f'Chave: {chave}: {valor}')
    soma = sum(dicionarios.values())
    media = soma / len(dicionarios)
    print(f'\nSoma dos Valores: {soma:.2f}')
    print(f'Média dos Valores: {media:.2f}')

leitura()

