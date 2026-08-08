''' 
Programa: organizando_notas.py
'''
import os

notas = [85, 70, 90, 60, 75]

def organizar_notas():
    print("Notas originais: ", notas)
    notas_ordenadas = notas.sort()
    print("Notas organizadas em ordem crescente: ", notas)
    return notas_ordenadas

def main():
    organizar_notas()

if __name__ == "__main__":
    main()

