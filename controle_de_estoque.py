'''
Verifica se o produto está disponível em estoque e retorna a quantidade disponível
utilizando WHILE
'''
import os

estoque = {
    "Arroz": 10,
    "Feijão": 5,
    "Macarrão": 8,
    "Açúcar": 12,
    "Sal": 15
}

def lista_produtos():
    print("Produtos disponíveis em estoque:")
    for idx, (produto, quantidade) in enumerate(estoque.items(), start=1):
        print(f"{idx}. {produto}: {quantidade} unidades")
    print('\n')

def processamento():
    qtde_indice_erro = 0

    while True:
            produto = input("Digite o índice do produto que deseja comprar: ")

            if produto.isdigit() and 1 <= int(produto) <= len(estoque):
                produto = list(estoque.keys())[int(produto) - 1]
                print(f"O produto '{produto}' está disponível em estoque. Quantidade: {estoque[produto]}")

                quantidade = int(input(f"Qual a quantidade de {produto} que deseja comprar? "))
                calcula_estoque(produto, quantidade)
                print('\n')
                break

            qtde_indice_erro += 1
            print(f"Índice inválido. Tentativa {qtde_indice_erro} de 3.")

            if qtde_indice_erro >= 3:
                print("Número máximo de tentativas excedido.")
                break

def calcula_estoque(produto, quantidade):
    if quantidade <= estoque[produto]:
        estoque[produto] -= quantidade
        print(f"Compra realizada com sucesso! Quantidade restante de {produto}: {estoque[produto]}")
    else:
        print(f"Quantidade solicitada maior que a disponível em estoque. Quantidade disponível: {estoque[produto]}")

def termino():
    while True:
        resposta = input("Deseja encerrar o programa? (s/n): ").lower()
        if resposta == 's':
            break
        elif resposta == 'n':
            lista_produtos()
            processamento()
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")
    print("Programa encerrado.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    lista_produtos()
    processamento()
    termino()

if __name__ == "__main__":
    main()