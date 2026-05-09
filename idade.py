# Programa para verificar a idade de uma pessoa
import os

def verifica_idade():
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <=12:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você tem {idade} anos. Você é uma criança.\n")
    elif 13 <= idade <= 17:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você tem {idade} anos. Você é um adolescente.\n")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você tem {idade} anos. Você é um adulto.\n")

def main():
    verifica_idade()

if __name__ == "__main__":
    main()

