'''
Descrição: Este programa organiza o portfólio de projetos 
Programa: organizando_portifolio.py
'''
import os
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# Processamento dos dados
def processamento():
    print("Projetos em andamento:")
    for projeto in projetos:
        if projeto is not None:
            print(f"- {projeto}")
        else:
            print("- Projeto sem nome")

# Termino do Programa
def termino():
    print("\nPortfólio organizado com sucesso.")

# Inicio do Programa
def main():
    os.system("cls")
    print("Portfólio de Projetos:")
    processamento()
    termino()

if __name__ == "__main__":
    main()