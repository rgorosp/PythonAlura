"""
Procura um livro pelo título.
Programa. procurar_livro.py
"""
import os

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

def procurar_livro(titulo):
    """
    Procura um livro pelo título na lista de livros.
    :param titulo: Título do livro a ser procurado.
    :return: Mensagem indicando se o livro foi encontrado ou não.
    """
    if titulo in livros:
        return f"O livro '{titulo}' foi encontrado."
    else:
        return f"O livro '{titulo}' não foi encontrado."

def termino():
    print ("Programa encerrado.")
    
    
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo = input("Digite o título do livro que deseja procurar: ")
    print(procurar_livro(titulo))
    termino()

if __name__ == "__main__":
    main()

