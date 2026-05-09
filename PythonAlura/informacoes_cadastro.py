# Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
# Programa: informacoes_cadastro.py
import os

pessoa = [{
    'Nome': 'João',
    'Idade': 30,
    'Cidade': 'São Paulo',
    'Profissão': 'Engenheiro'
}]

continuar = True

# MENU PRINCIPAL
def menu_principal():
    print(""" """)
    print("------------------------------------------------")
    print("         𝕭𝖊𝖒 Vindo a Lojas Marizetes")
    print("------------------------------------------------")
    print("1. Cadastrar Clientes")
    print("2. Listar Clientes")
    print("3. Atualizar Clientes")
    print("4. Excluir Clientes")
    print("5. Sair")
    print("------------------------------------------------\n")
    escolha = input("Digite a opção desejada: ")
    if escolha == '1':
        cadastrar_clientes()
    elif escolha == '2':
        listar_clientes()
    elif escolha == '3':
        atualizar_clientes()
    elif escolha == '4':
        excluir_clientes()
    elif escolha == '5':
        termino()
        return False
    else:
        termino()   

# PROCESSAMENTO DOS DADOS
def processamento():
    relatorio("Informações do Cadastro")
    for chave, valor in pessoa[0].items():
        print(f"{chave}: {valor}")
    print()

# CADASTRO DO CLIENTE
def cadastrar_clientes():
    while True:
        relatorio("Cadastrar Cliente")
        nome_cliente = input("Digite o nome do cliente: ")
        idade_cliente = input("Digite a idade do cliente: ")
        cidade_cliente = input("Digite a cidade do cliente: ")
        profissao_cliente = input("Digite a profissão do cliente: ")
        pessoa.append({'Nome': nome_cliente, 'Idade': idade_cliente, 'Cidade': cidade_cliente, 'Profissão': profissao_cliente})
        print(f"Cliente '{nome_cliente}' cadastrado com sucesso!\n")
        print()
        menu_principal()

        flag = input("Deseja cadastrar outro cliente? (s/n): ").lower()
        if flag == 's':
            continue
        else:
            print()
            menu_principal()

def listar_clientes():
    relatorio("Lista de Clientes Cadastrados")
    listar_clientes1()
    print()
    menu_principal()
    
def listar_clientes1():
    for idx, cliente in enumerate(pessoa, start=1):
        print(f"{idx}. Nome: {cliente['Nome']}, Idade: {cliente['Idade']}, Cidade: {cliente['Cidade']}, Profissão: {cliente['Profissão']}")

# ATUALIZAR CADASTRO DO CLIENTE
def atualizar_clientes():
    relatorio("Atualizar Lista de Clientes")
    listar_clientes1()
    try:
        indice = int(input("Digite o número do cliente que deseja atualizar: ")) - 1
        if 0 <= indice < len(pessoa):
            nome_cliente = input("Digite o novo nome do cliente: ")
            idade_cliente = input("Digite a nova idade do cliente: ")
            cidade_cliente = input("Digite a nova cidade do cliente: ")
            profissao_cliente = input("Digite a nova profissão do cliente: ")
            pessoa[indice] = {'Nome': nome_cliente, 'Idade': idade_cliente, 'Cidade': cidade_cliente, 
            'Profissão': profissao_cliente}
            print(f"Cliente '{nome_cliente}' atualizado com sucesso!\n")
        else:
            print("Número de cliente inválido.\n")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.\n")

    print()
    menu_principal()

# EXCLUIR CADASTRO DO CLIENTE
def excluir_clientes():
    relatorio("Excluir Cliente")
    listar_clientes1()
    try:
        indice = int(input("Digite o número do cliente que deseja excluir: ")) - 1
        if 0 <= indice < len(pessoa):
            cliente_excluido = pessoa.pop(indice)
            print(f"Cliente '{cliente_excluido['Nome']}' excluído com sucesso!\n")
        else:
            print("Número de cliente inválido.\n")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.\n")

    print()
    menu_principal()

# FINALIZANDO O APLICATIVO
def termino():
    relatorio("Encerrando o Cadastro")
    print("Obrigado por usar o sistema de cadastro! Até a próxima!\n")

# Função para imprimir um subtítulo formatado
def relatorio(subtitulo):
    print("-" * len(subtitulo))
    print(f"{subtitulo}")
    print("-" * len(subtitulo))

# INICIO DO PROGRAMA PRINCIPAL
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        continuar = menu_principal()
        if not continuar:
            break

if __name__ == "__main__":
    main()