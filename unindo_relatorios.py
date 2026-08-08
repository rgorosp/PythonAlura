''' 
Programa: unindo_relatorios.py
Descritivo: Une os relatórios de diferentes fontes.
'''
import os

lista1 = ["arroz", "feijão", "macarrão", "óleo", "sal"]
lista2 = ["batata", "cenoura", "tomate", "alface", "pepino"]

def unir_listas():
    lista_unida = lista1 + lista2
    print("Lista unida: ", lista_unida)
    return lista_unida

def main():
    unir_listas()
    print("\nFim do programa.")

if __name__ == "__main__":
    main()