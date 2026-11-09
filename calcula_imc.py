'''
Calcula o Índice de Massa Corporal (IMC) a partir do peso e altura fornecidos pelo usuário.
O IMC é calculado pela fórmula: IMC = peso / (altura ** 2)
'''
import os

def receba():
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))
    return peso, altura

def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    peso, altura = receba()
    imc = calcula_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print("Você está com o peso normal.")
    elif 25 <= imc < 29.9:
        print("Você está com sobrepeso.")
    else:
        print("Você está com obesidade.")       