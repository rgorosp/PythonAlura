'''
Tabuada de um número
'''
import os

def leitura(mensagem):
    return int(input(mensagem))

def imprimir(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = leitura("Digite um número para ver a tabuada: ")
imprimir(numero)
