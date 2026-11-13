'''
Programa que recebe três valores e calcula a média.
'''
import os

def receba(msg):
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = int(input(msg))
    return valor

def calcula_media(a, b, c):
    return (a + b + c) / 3

if __name__ == "__main__":
    a = receba("Digite o Primeiro Valor: ")
    b = receba("Digite o Segundo Valor: ")
    c = receba("Digite o Terceiro Valor: ")
    resultado = calcula_media(a, b, c)
    print("A Média é: ", resultado)