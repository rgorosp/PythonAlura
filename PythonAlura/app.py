"""
Criação de um Menu de um Restaurante
"""
import os

lista_de_restaurantes = [{"Nome": "Fujimae","Categoria": "Japonesa","Ativo": False},
                         {"Nome": "Formosa","Categoria": "Pizzaria","Ativo": True},
                         {"Nome": "Saboroso","Categoria": "Brasileira","Ativo": False}]

# TELA PRINCIPAL
def tela_principal():
    print(""" """)
    print("------------------------------------------------")
    print("         𝕭𝖊𝖒 𝖛𝖎𝖓𝖉𝖔 𝖆𝖔 𝕾𝖆𝖇𝖔𝖗 𝕰𝖝𝖕𝖗𝖊𝖘𝖘")
    print("------------------------------------------------")
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair")
    print("------------------------------------------------\n")

def opcao_invalida():
    print("Entrada inválida. Por favor, digite um número.\n")

# MENU DE OPÇÕES
def opcoes_menu():
    try:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            lista_restaurantes()
        elif opcao == 3:
            ativar_restaurante()
        elif opcao == 4:
            finalizando_app()
            return False
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.\n")
    except ValueError:
        opcao_invalida()
    return True

# FINALIZANDO O APLICATIVO 
def finalizando_app():
    imprimindo_subtitulo("Finalizando o aplicativo...")
    print("Obrigado por usar o Sabor Express! Até a próxima!\n")

# CADASTRO DE RESTAURANTE
def cadastrar_restaurante():
    imprimindo_subtitulo("Opção 1 selecionada: Cadastrar Restaurante")

    nome_restaurante = input("Digite o nome do restaurante: ")
    categoria_restaurante = input("Digite a categoria do restaurante: ")
    lista_de_restaurantes.append({"Nome": nome_restaurante, "Categoria": categoria_restaurante, "Ativo": False})
    print(f"Restaurante '{nome_restaurante}' cadastrado com sucesso!\n")
    print("Deseja cadastrar outro restaurante? (s/n)")
    continuar = input().lower()
    if continuar == 's':
        cadastrar_restaurante()

# LISTA DE RESTAURANTES
def lista_restaurantes():
    imprimindo_subtitulo("Opção 2 selecionada: Listar Restaurantes")

    if not lista_de_restaurantes:
        print("Nenhum restaurante cadastrado.\n")
    else:
        print("Restaurantes cadastrados:")
        print("-" * 60)
        print(f"{'Nº'.ljust(6)}. {'Nome'.ljust(20)} {'Categoria'.ljust(22)} {'Status'}")
        print("-" * 60)
        for idx, restaurante in enumerate(lista_de_restaurantes, start=1):
            nome_restaurante = restaurante["Nome"] 
            categoria_restaurante = restaurante["Categoria"]
            ativo_restaurante = restaurante["Ativo"]
            print(f"{str(idx).ljust(5)}. {nome_restaurante.ljust(20)} - {categoria_restaurante.ljust(20)} - {'Ativo' if ativo_restaurante else 'Inativo'}")
        print()

def ativar_restaurante():
    imprimindo_subtitulo("Opção 3 selecionada: Ativar Restaurante")

    if not lista_de_restaurantes:
        print("Nenhum restaurante cadastrado para ativar.\n")
    else:
        print("Restaurantes disponíveis para ativação:")
        for idx, restaurante in enumerate(lista_de_restaurantes, start=1):
            nome_restaurante = restaurante["Nome"]
            print(f"{idx}. {nome_restaurante}")
        try:
            print() 
            escolha = int(input("Digite o número do restaurante que deseja ativar/desativar: "))
            if 1 <= escolha <= len(lista_de_restaurantes):
                restaurante_ativado = lista_de_restaurantes[escolha - 1]
                restaurante_ativado["Ativo"] = not restaurante_ativado["Ativo"]
                status = "ativado" if restaurante_ativado["Ativo"] else "desativado"
                print(f"Restaurante '{restaurante_ativado}' {status} com sucesso!\n")
            else:
                print("Número inválido. Por favor, selecione um número válido.\n")
        except ValueError:
            opcao_invalida()

def imprimindo_subtitulo(subtitulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    relatorio = "*" * len(subtitulo)
    print(relatorio)
    print(f"{subtitulo}")
    print(relatorio)

# INICIO DO PROGRAMA PRINCIPAL
def main():
    while True:
        tela_principal()
        continuar = opcoes_menu()
        if not continuar:
            break

if __name__ == "__main__":
    main()