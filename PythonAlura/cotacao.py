"""
Programa: cotacao.py
author: Emerson
Descritivo: Conversor de moedas. Receber do usuário o valor em reais(R$) 
e o sistema precisa mostrar quanto isso representa em dólares (US$), 
usando uma taxa de câmbio definida pela empresa.
"""
import os 

valorDolarHoje = 5.287
taxaIof = 1.1

# PROCESSAMENTO DOS DADOS
def processamento():
    valorReal = float(input("Digite o valor em R$ Real: "))

    calculo = valorReal / valorDolarHoje
    descontoIof = taxaIof / 100
    desconto = calculo * descontoIof
    calculo = calculo - desconto

    print(f'Valor R$ {valorReal:.2f} a receber em US$ {calculo:.3f}')

    print('\nFim do Programa')

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento()

if __name__ == "__main__":
    main()

