'''
Programa Calcula Distancia e Consumo de Combustível
'''
import os

def leitura(msg):
    print(msg)
    valor = int(input())
    return valor

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def resultado(tempo, velocidade, distancia, litros):
    print(f"Tempo: {tempo}")
    print(f"Velocidade: {velocidade}")
    print(f"Distancia: {distancia}")
    print(f"Litros: {litros}")

def calcula_litros(distancia):
    return distancia / 12

if __name__ == "__main__":
    tempo = leitura("Digite o Tempo Gasto na Viagem: ")
    velocidade = leitura("Digite o Limite da Velocidade: ")
    distancia = calcula_distancia(tempo, velocidade)
    litros = calcula_litros(distancia)
    resultado(tempo, velocidade, distancia, litros)
