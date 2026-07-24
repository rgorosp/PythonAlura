'''
Programa: ajustando_nomes_produtos.py
Descritivo: Recebe o nome dos produtos, retire os espaços em branco e
retorna uma lista de produtos ajustados classificados em ordem alfabética.
A primeira letra de cada produto deve ser maiúscula e o restante minúscula.
'''
import os

produtos = []

# Processamento do programa
def processamento():
    while True:
        produto = input("Digite o nome do produto (digite 'sair' para encerrar): ").strip()
        if produto == "sair":
            break
        if not produto:
            continue
        produtos.append(produto)

    produtos_ajustados = [produto.capitalize() for produto in produtos]
    produtos_ajustados.sort()

    print("Produtos ajustados:")
    for produto in produtos_ajustados:
        print(produto)    

# Termino do processamento
def termino():
    print("\nFim do Programa")

# Inicio do programa
def main():
    os.system('cls')
    processamento()
    termino()

if __name__ == "__main__":
    main()