'''
Programa: biblioteca.py
Descritivo: Programa de leitura de Titulos de Filmes, aonde ele ira ler 
o titulo, e identificar todas as palavras iniciadas por uma determinada
letra.

A solução utiliza o módulo re (Expressões Regulares) e a função re.findall(), 
que retorna uma lista com todas as ocorrências encontradas.
'''
import re, os

programa = 'biblioteca.py'
resultado = ''

# Processamento do Programa
def processamento():
    titulo = input("Digite o título do livro: ")
    letra = input("Digite a letra inicial para pesquisa: ").strip()

    # Procura todas as palavras que começam com a letra informada
    padrao = rf"\b{re.escape(letra)}\w*"

    resultado = re.findall(padrao, titulo, flags=re.IGNORECASE)

    print(resultado)

# Termino do Programa
def termino():
    print(f'\nTermino do Programa: {programa}\n')
    os._exit(0)

# Inicio do Programa
def main():
    os.system("cls" if os.name == "nt" else "clear")
    processamento()
    termino()

if __name__ == "__main__":
    main()

