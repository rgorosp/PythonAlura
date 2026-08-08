''' 
Programa: itens_despensa.py 
Descritivo: Verifica se o item está na despensa, caso necessário, avisar
que precisa comprar o item.
'''
import os 

lista = ["arroz", "feijão", "macarrão", "óleo", "sal"]

def despensa():
    item = input("Digite o item que deseja verificar na despensa: ").strip().lower()

    if item in lista:
        print(f"O item '{item}' está disponível na despensa.")
    else:
        print(f"O item '{item}' não está disponível na despensa. Você precisa comprar este item.")
        while True:
            resposta = input("Deseja adicionar o item a lista de compras? (s/n): ").strip().lower()
            if resposta == "s":
                lista.append(item)
                print(f"O item '{item}' foi adicionado à lista de compras.")
                print(f"Lista de compras atualizada: {lista}")
                break
            elif resposta == "n":
                print("Você optou por não adicionar o item à lista de compras.")
                break
            else:
                print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

def termino():
    print("\nFim do programa.")


def main():
     despensa()
     termino()

if __name__ == "__main__":
    main()
