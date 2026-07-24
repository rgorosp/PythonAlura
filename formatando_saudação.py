'''
Programa: formatando_saudação.py
Descritivo: Programa recebe o nome do usuário  e estado e retorna uma saudação formatada.
'''
import os 

def processamento():
    nome = input("Digite seu nome: ").strip()
    estado = input("Digite seu estado: ").strip()

    if not nome or not estado:
        print("Nome ou estado não podem ser vazios.")
        return

    saudacao = f"Olá, {nome.title()}! Bem-vindo(a) ao estado de {estado.title()}."
    print(saudacao)

def termino():
    print("\nFim do programa.")

def main():
    os.system('cls')
    processamento()
    termino() 

if __name__ == "__main__":
    main()

