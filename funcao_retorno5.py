'''
Exemplo de função com retorno e docstring (help).
'''
import os

def graus_celsius_para_fahrenheit(graus_celsius):
    '''
    Converte uma temperatura de graus Celsius para Fahrenheit.

    Parâmetros:
    graus_celsius (float): Temperatura em graus Celsius.

    Retorna:
    float: Temperatura em graus Fahrenheit.
    '''
    return (graus_celsius * 9/5) + 32


# Limpa a tela UMA vez, no início do programa
os.system('cls' if os.name == 'nt' else 'clear')

# Mostra a documentação da função
help(graus_celsius_para_fahrenheit)
os.system('pause')

# Usa a função
r = graus_celsius_para_fahrenheit(float(input("Digite a Temperatura em Celsius: ")))
print(f'{r} graus Fahrenheit')
