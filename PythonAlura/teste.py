"""
TESTE
"""
lista_de_numeros = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]
lista_quatro_nomes = ["Ana", "Bruno", "Carlos", "Diana"]
lista_anonasc_anoatual = [1975, 2026]

def imprimir_subtitulo(subtitulo):
    print() 
    print(f"{subtitulo}")

def teste_listas():
    imprimir_subtitulo("Lista de Números")
    for numero in lista_de_numeros:
        print(numero)
    print()
    for i in range(len(lista_de_numeros)):
        print(f"Índice: {i} - Valor: {lista_de_numeros[i]}")

def teste_listas_nomes():
    imprimir_subtitulo("Lista de Nomes")
    for nome in lista_quatro_nomes:
        print(nome)

def teste_listas_anoatual():
    imprimir_subtitulo("Lista de Anos")
    print(f'Ano_Nascimento: {lista_anonasc_anoatual[0]} - Ano_Atual: {lista_anonasc_anoatual[1]}')
    print(f'Idade: {lista_anonasc_anoatual[1] - lista_anonasc_anoatual[0]} anos.')

def teste_calculo_numeros_impares():
    imprimir_subtitulo("Números Ímpares")
    calculo = 0
    for numero in lista_de_numeros:
        if numero % 2 != 0:
            calculo = calculo + numero  
            print(f'Calculo: {calculo} - Número: {numero}')
        else:
            continue

def teste_imprimir_lista_decrescente():
    imprimir_subtitulo("Lista de Números em Ordem Decrescente")
    for numero in reversed(lista_de_numeros):
        print(numero)

def teste_imprimir_tabuada():
    tabuada = int(input("Digite um número para ver a tabuada: "))
    imprimir_subtitulo(f"Tabuada do {tabuada}")
    for i in range(1, 11):
        resultado = tabuada * i
        print(f"{tabuada} x {i} = {resultado}")

def teste_soma_lista_numeros_com_for_try_except():
    imprimir_subtitulo("Soma dos Números da Lista")
    soma = 0
    try:
        for numero in lista_de_numeros:
            soma += numero
        print(f"A soma dos números da lista é: {soma}")
    except TypeError:
        print("Erro: A lista contém um valor que não é um número.")

def teste_calculo_media_lista_numeros_com_for_try_except():
    imprimir_subtitulo("Cálculo da Média dos Números da Lista")
    soma = 0
    try:
        for numero in lista_de_numeros:
            soma += numero
        media = soma / len(lista_de_numeros)
        print(f"A média dos números da lista é: {media}")
    except TypeError:
        print("Erro: A lista contém um valor que não é um número.")
    except ZeroDivisionError:
        print("Erro: A lista está vazia, não é possível calcular a média.")

def main():
    teste_listas()
    teste_listas_nomes()
    teste_listas_anoatual()
    teste_calculo_numeros_impares()
    teste_imprimir_lista_decrescente()
    teste_imprimir_tabuada()
    teste_soma_lista_numeros_com_for_try_except()
    teste_calculo_media_lista_numeros_com_for_try_except()

if __name__ == "__main__":
    main()