'''
Este programa realiza operações matemáticas básicas entre dois números fornecidos pelo usuário.
As operações incluem soma, subtração, multiplicação, divisão e cálculo 
de resto da divisão.
'''
import os

def leitura(msg):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(msg) 
    valor = int(input())
    return valor

def calculo(iA, iB):
    soma = iA + iB
    print(f"A soma de {iA} e {iB} é {soma}")
    subtracao = iA - iB
    print(f"A subtração de {iA} e {iB} é {subtracao}")
    multiplicacao = iA * iB
    print(f"A multiplicação de {iA} e {iB} é {multiplicacao}")
    divisao = iA / iB
    print(f"A divisão de {iA} e {iB} é {divisao}")
    resto = iA % iB
    print(f"O resto da divisão de {iA} e {iB} é {resto}")

if __name__ == "__main__":
    iA = leitura("Digite um valor: ")
    iB = leitura("Digite outro valor: ")
    calculo(iA, iB)
    termino = input("\nPressione Enter para finalizar...")


