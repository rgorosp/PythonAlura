'''
Cálculo do valor do pedágio com base na distância percorrida.
'''
import os

def distancia_percorrida(mensagem):
    distancia = float(input(mensagem))

    valor_pedagio = 0
    if (distancia <= 100):
        valor_pedagio = distancia * 0.25
    elif (distancia > 100 and distancia <= 200):
        valor_pedagio = distancia * 0.20
    else:
        valor_pedagio = distancia * 0.15
    print(f"Valor do pedágio: R$ {valor_pedagio:.2f}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    distancia_percorrida("Digite a distância percorrida: ")