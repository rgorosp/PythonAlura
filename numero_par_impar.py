# Programa para verificar se um número é par ou ímpar
import os
def par_impar():
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"O número {numero} é par.\n")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"O número {numero} é ímpar.\n")

def main():
    par_impar()

if __name__ == "__main__":
    main()
