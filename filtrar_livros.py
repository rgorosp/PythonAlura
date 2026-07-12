'''
Programa: filtrar_livros.py
Descrição: Filtra livros com base em critérios específicos.
'''
import os

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

# Função para filtrar livros com estoque maior que zero
def processamento():
    titulo = 'Livros disponíveis em estoque'
    len_titulo = len(titulo)
    livros_disponiveis = [livro for livro in livros if livro["estoque"] > 0]
    if livros_disponiveis:
        print(len_titulo * "=")
        print(titulo)
        print(len_titulo * "=")
        for livro in livros_disponiveis:
            print(f"- {livro['nome']} (Estoque: {livro['estoque']})")
    else:
        print("Nenhum livro disponível em estoque.")

# Função para encerrar o programa
def termino():
    print("Programa encerrado.")
   
# INICIO DO PROGRAMA
def main(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento()
    termino()

if __name__ == "__main__":
    main()