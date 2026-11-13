'''
Programa que recebe um valor e valida se é positivo.
'''
import os

def receba(valor):
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = int(input("Digite o Valor: "))
    return valor

def valida(vlr):
    if vlr < 0:
        return False
    else:
        return True
    
vlr = receba(valor=0)
resultado = valida(vlr)
print("Resultado da Validação: ", resultado)