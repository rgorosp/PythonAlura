'''
Exemplo de função com retorno e função de início.
A função soma retorna a soma de dois números.
A função inicio chama a função soma e imprime o resultado.
'''
import os

def soma(a, b):
    return a + b

def inicio():
    os.system('cls' if os.name == 'nt' else 'clear')
    resultado = soma(3, 4)
    print("Resultado 1: ", resultado)

def inicio1(msg):
    a = int(input(msg))
    b = int(input(msg))
    resultado = soma(a, b)
    return resultado

inicio()
resultado = inicio1("Digite o Valor: ")
print("Resultado 2: ", resultado)