'''
Exemplo de iteração sobre uma lista com índices e valores'''
import os
import numpy as np

listas = []

def leitura():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            listas.append(int(input("Digite um número: ")))
            print("Número adicionado com sucesso.")
            print("Deseja adicionar outro número? (s/n)")
            resposta = input().strip().lower()
            if resposta != 's':
                imprimir()
                break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def imprimir():
    for i, item in enumerate(listas):
        print(f'Index {i}: {item}')
    print(f'\nSoma dos Valores: {sum(listas)}')

leitura()


