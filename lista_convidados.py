''' 
Programa: lista_convidados.py
Descrição: Este programa permite que o usuario insira os convidados
e imprime no final a lista classificada em ordem alfabética.
'''
import os

lista_convidados = ['Ana', 'Pedro', 'Carlos']

def processamento():
    while True:
        print('*' * 50)
        print("Programa de lista de convidados!")
        print('*' * 50)
        print(' 1 - Listar convidados')
        print(' 2 - Adicionar convidado')
        print(' 3 - Remover convidado')
        print(' 4 - Sair')
        print('*' * 50)

        print("\nDigite o número da opção desejada:")
        opcao = input()

        if opcao == '1':
            print("\nLista de convidados:")
            for convidado in lista_convidados:
                print(convidado)
        elif opcao == '2':
            print("\nDigite o nome do convidado a ser adicionado:")
            nome = input()
            lista_convidados.append(nome)
            print(f"{nome} foi adicionado à lista de convidados.")
        elif opcao == '3':
            print("\nDigite o nome do convidado a ser removido:")
            nome = input()
            if nome in lista_convidados:
                lista_convidados.remove(nome)
                print(f"{nome} foi removido da lista de convidados.")
            else:
                print(f"{nome} não está na lista de convidados.")
        elif opcao == '4':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def termino():
    print("\nLista de convidados em ordem alfabética:")
    for convidado in sorted(lista_convidados):
        print(convidado)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento()
    termino()

if __name__ == "__main__":
    main()
