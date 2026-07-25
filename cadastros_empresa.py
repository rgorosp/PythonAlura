''' 
Programa: cadastros_empresa.py
Descritivo: O padrão esperado é que os nomes comecem com uma letra maiúscula
e contenham apenas letras (sem números ou caracteres especiais).
O programa usa o REGEX para validar os nomes e exibe uma mensagem de erro
caso o nome não esteja no padrão esperado. 
'''
import os
import re 

def validar_nome(nome):
    particulas = {"da", "de", "do", "das", "dos", "e"}
    partes = nome.split()

    if not partes:
        return False

    # Primeira palavra obrigatoriamente inicia com maiúscula
    if not (partes[0][0].isupper() and partes[0].isalpha()):
        return False

    for parte in partes[1:]:
        if parte.lower() in particulas:
            continue
        if not (parte[0].isupper() and parte.isalpha()):
            return False

    return True

def processamento():
    while True:

        nome = input("Digite o nome do cliente (ou 'sair' para encerrar): ")

        if nome.lower() == "sair":
            break

        partes = nome.split()

        valido = validar_nome(nome)
        if valido:
            print(f"Nome '{nome}' válido.")
        else:
            print("Erro: O nome deve conter apenas letras e cada palavra deve iniciar com letra maiúscula.")

def termino():
    print("Encerrando o programa...")
    os._exit(0)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    processamento()
    termino()

if __name__ == "__main__":
    main()