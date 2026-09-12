'''
Programa: lista_de_compras.py
Descrição: Receba a lista de compras de 2 pessoas e imprima apenas 
os produtos que ambas compraram.
'''
import os

def processamento():
    lista1 = [produto.strip().casefold() for produto in input(
        "Digite os produtos da primeira pessoa, separados por vírgula: "
    ).split(",")]
    lista2 = [produto.strip().casefold() for produto in input(
        "Digite os produtos da segunda pessoa, separados por vírgula: "
    ).split(",")]
    produtos_comuns = set(lista1) & set(lista2)
    print("Produtos que ambas compraram:", ", ".join(sorted(produtos_comuns)))

def termino():
    print("Fim do programa.")
    os._exit(0)

def main():
    processamento()
    termino()

if __name__ == "__main__":
    main()
