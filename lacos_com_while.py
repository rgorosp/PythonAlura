'''
Lacos com while
Programa: lacos_com_while.py
'''
import os

# processamento dos jobs com laços de repetição
def processamento_while():
    contador = 0 
    while contador < 5:
        print(f'"Bem-vindo ao Buscante!"')
        contador += 1           

# Termino do Programa
def termino():
    print("\nProcessamento concluído.")

# Inicio do Programa
def main():
    os.system("cls")
    processamento_while()
    termino()

if __name__ == "__main__":
    main()