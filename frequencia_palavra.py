# Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
# Programa: frequencia_palavra.py
import os

# FUNÇÃO PARA CONTAR A FREQUÊNCIA DE PALAVRAS EM UMA FRASE
def contar_frequencia_palavras(frase):
    palavras = frase.split()
    frequencia = {}
    for palavra in palavras:
        palavra = palavra.lower()  # Convertendo para minúsculas para contar de forma case-insensitive
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

# FUNÇÃO PARA IMPRIMIR A FREQUÊNCIA DE PALAVRAS NO TERMINAL
def imprimir_frequencia(frequencia):
    print("\nFrequência de palavras:")
    print("-" * 30)
    for palavra, contagem in frequencia.items():
        print(f"{palavra}: {contagem}")
    print("-" * 30)

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    frase = input("Digite uma frase: ")
    frequencia = contar_frequencia_palavras(frase)
    imprimir_frequencia(frequencia)

if __name__ == "__main__":
    main()