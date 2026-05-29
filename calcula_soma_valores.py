'''
Descrição: Este programa calcula a soma de uma lista de valores fornecida pelo usuário.
Programa: calcula_soma_valores.py
'''
import os

valores = [10, 20, 30, 40, 50]

# Processamento dos dados
def processamento():
    soma = sum(valores)
    print(f"A soma dos valores é: {soma}")

# Termino do Programa
def termino():
    print("\nProcessamento concluído.")

# Inicio do Programa
def main():
    os.system("cls")
    processamento()
    termino()

if __name__ == "__main__":
    main()
