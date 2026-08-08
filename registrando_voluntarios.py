'''
Programa: registrando_voluntarios.py
Descritivo: Registra informações de voluntários para um evento.
'''
import os

nomes = []

def registrar_voluntario():
    while True:
        nome = input("Digite o Nome do voluntário ou (sair) para encerrar: ")
        if nome.lower() == "sair":
            return False
        else:
            if nome in nomes:
                print("Este voluntário já está registrado.")
            else:
                nomes.append(nome)
                continue    

def exibir_voluntarios():
    if not nomes:
        print("Nenhum voluntário registrado.")
    else:
        print("\nLista de voluntários registrados:")
        for i, nome in enumerate(nomes, start=1):
            print(f"{i}. {nome}")

def main():
    registrar_voluntario()
    exibir_voluntarios()
    print("\nFim do programa.")
    os._exit(0)

if __name__ == "__main__":
    main()
