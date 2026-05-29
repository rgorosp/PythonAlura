"""
Lacos de repetição   
Programa: lacos_de_repeticao.py
"""
import os

nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

# Cria o processo de processamento dos jobs com laços de repetição
def processamento_for():
    for nome in nomes:
        print(f"Olá, {nome}!")

def processamento_while():
    print(" ")
    i = 0
    while i < len(nomes):
        print(f"Olá, {nomes[i]}!")
        i += 1

# INICIO DO PROGRAMA
def main():
    os.system("cls")
    processamento_for()
    processamento_while()

if __name__ == "__main__":
    main()