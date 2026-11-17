# Programa para verificar a idade de uma pessoa
import os

def leitura(mensagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    return int(input(mensagem))

def verifica_idade():
    idade = leitura("Digite sua idade: ")
    if 0 <= idade <=12:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você tem {idade} anos. Você é uma criança.\n")
    elif 13 <= idade <= 17:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você tem {idade} anos. Você é um adolescente.\n")
    elif 18 <= idade <= 200:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você tem {idade} anos. Você é um adulto.\n")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Idade inválida.\n")

def main():
    verifica_idade()

if __name__ == "__main__":
    main()

