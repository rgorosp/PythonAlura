'''
Programa: vendas_por_categoria.py
Descrição: Faça uma lista de dicionarios, aonde minha lista de vendas 
tenha 3 chaves por categoria: Eletrônicos, Eletrodomésticos e livros. 
A lista deve conter o nome do produto, a quantidade vendida e o valor
unitario. Escreva um menu com as 3 opções de categoria, e liste no final
o valor total de cada categoria.
'''
import os 

vendas = {
    "Eletrônicos": [],
    "Eletrodomésticos": [],
    "Livros": []
}

def processamento():
    for categoria, itens in vendas.items():
        total = sum(item["quantidade"] * item["valor_unitario"] for item in itens)
        print(f"Total de {categoria}: R$ {total:.2f}")

def listar_vendas(categoria):
    if not vendas[categoria]:
        print("Nenhuma venda cadastrada.")
        return

    for item in vendas[categoria]:
        print(f"{item['nome']} - Quantidade: {item['quantidade']} - Valor Unitário: R$ {item['valor_unitario']:.2f}")

def incluir_venda():
    categorias = list(vendas)
    print("\nCategorias:")
    for indice, categoria in enumerate(categorias, start=1):
        print(f"{indice}. {categoria}")

    categoria_escolhida = input("Escolha a categoria: ")
    try:
        categoria = categorias[int(categoria_escolhida) - 1]
    except (ValueError, IndexError):
        print("Categoria inválida.")
        return

    nome = input("Digite o nome do produto: ").strip()
    try:
        quantidade = int(input("Digite a quantidade vendida: "))
        valor_unitario = float(input("Digite o valor unitário: ").replace(",", "."))
    except ValueError:
        print("Quantidade e valor unitário devem ser numéricos.")
        return

    vendas[categoria].append({
        "nome": nome,
        "quantidade": quantidade,
        "valor_unitario": valor_unitario
    })
    print("Venda incluída com sucesso.")

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Menu de Categorias:")
    print("1. Eletrônicos")
    print("2. Eletrodomésticos")
    print("3. Livros")
    print("4. Incluir venda")
    print("0. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "0":
            break
        elif opcao == "1":
            print("Eletrônicos:")
            listar_vendas("Eletrônicos")
        elif opcao == "2":
            print("Eletrodomésticos:")
            listar_vendas("Eletrodomésticos")
        elif opcao == "3":
            print("Livros:")
            listar_vendas("Livros")
        elif opcao == "4":
            incluir_venda()
        else:
            print("Opção inválida.")
        processamento()
        input("\nPressione Enter para voltar ao menu...")
