'''
Programa: expressoes_regulares.py
Descritivo: Programa recebe um texto e retorna o endereço de email encontrado no texto.
'''
import os
import re

# FUNÇÃO QUE IMPRIME A MENSAGEM DE TÉRMINO
def processamento():
    texto = 'O email de contato é contato@exemplo.com, ' \
            'e outro email é outro@exemplo.com'
    padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(padrao, texto)
    print("Emails encontrados:")
    for email in emails:
        print(email)

# termino do processamento
def termino():
    print("\nFim do Programa")

# INICIO DO PROGRAMA
def main():
    os.system('cls')
    processamento()
    termino()

if __name__ == "__main__":
    main()
