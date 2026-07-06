'''
Crie um programa que utilize um laço for para exibir as seguintes mensagens:
Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
'''
import os

def processamento():
    for i in range(10, 0, -1):
        if i % 2 == 0:
            print(f"Faltam apenas {i} segundos - Não perca essa oportunidade!")
        else:
            print(f"A contagem continua: {i} segundos restantes.")
    print("Aproveite a promoção agora!")

def termino():
    print("Programa encerrado.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento()
    termino()

if __name__ == "__main__":
    main()