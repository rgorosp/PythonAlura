"""_summary_
Solicite um nome de usuário e uma senha e use uma estrutura if else 
para verificar se o nome de usuário e a senha fornecidos correspondem 
aos valores esperados determinados por você.
 """
import os

# CONTROLE DE ACESSO
def controle_senha():
    controle = 0
    while True:
        nome_usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if nome_usuario == "alura" and senha == "123456":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acesso concedido. Bem-vindo, Alura!\n")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acesso negado. Nome de usuário ou senha incorretos.\n")
            controle += 1
            print(f'Tentativa {controle} de 3.\n')
            if controle >= 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Número máximo de tentativas atingido. Acesso bloqueado.\n")
                break

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    controle_senha()

if __name__ == "__main__":
    main()

