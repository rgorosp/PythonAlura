# Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
# Programa: numeros_quadrados.py
import os

numeros_quadrados = {1: 1**2, 2: 2**2, 3: 3**2, 4: 4**2, 5: 5**2}

# FUNÇÃO PARA IMPRIMIR OS NÚMEROS E SEUS QUADRADOS
def imprimir_numeros_quadrados():
    imprimir_relatorio("Números e seus quadrados:")
    print("-" * 30)
    for numero, quadrado in numeros_quadrados.items():
        print(f"{numero}: {quadrado}")
    print("-" * 30)

# RELATORIO
def imprimir_relatorio(relatorio):
    print("*" * len(relatorio))
    print(relatorio)
    print("*" * len(relatorio))

def fim_programa():
    print("\nPrograma finalizado. Obrigado por usar!")
    while True:
        break

# INICIO DO PROGRAMA PRINCIPAL
def main(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    imprimir_numeros_quadrados()
    fim_programa()

if __name__ == "__main__":
    main()