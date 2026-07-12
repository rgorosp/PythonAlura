'''
Programa: valicacao_login.py
Descrição: Valida o login do usuário com base em credenciais pré-definidas.
Login deve conter 5 caracteres, e a senha deve conter 8 caracteres.
'''
import os

# Função para processar o login e senha do usuário
def processamento():
    acesso_login = True
    while acesso_login:
        login = input("Digite seu login (5 caracteres): ")
        if len(login) != 5:
            print("Login inválido. O login deve conter exatamente 5 caracteres.")
        else:
            print("Login válido. Acesso concedido.")
            acesso_login = False
            acesso_senha = True

    while acesso_senha:
        senha = input("Digite sua senha (8 caracteres): ")
        if len(senha) == 8:
            print("Senha válida. Acesso concedido.")
            acesso_senha = False
        else:
            print("Login ou senha inválidos. Acesso negado.")
        
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

