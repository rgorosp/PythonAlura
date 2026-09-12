'''
Programa: comparando_respostas.py
Descrição: Compara as respostas de duas pessoas e imprime retirando as duplicidades
'''
import os 

def remover_duplicidades(respostas):
    return list(dict.fromkeys(resposta for resposta in respostas if resposta))

def processamento():
    respostas1 = remover_duplicidades(resposta.strip().casefold() for resposta in input(
        "Digite as respostas da primeira pessoa, separadas por vírgula: "
    ).split(","))
    respostas2 = remover_duplicidades(resposta.strip().casefold() for resposta in input(
        "Digite as respostas da segunda pessoa, separadas por vírgula: "
    ).split(","))
    respostas_unicas = remover_duplicidades(respostas1 + respostas2)
    print("Respostas sem duplicidades:", ", ".join(respostas_unicas))

def termino():
    print("\nFim do programa.")
    os._exit(0)

def main():
    processamento()
    termino()

if __name__ == "__main__":
    main()