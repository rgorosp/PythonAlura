'''
Programa Calcula Distancia e Consumo de Combustível
'''
import os

def leitura(msg):
    '''
    Exibe uma mensagem e lê um número inteiro digitado pelo usuário.

    Parâmetros:
    msg (str): Mensagem exibida antes da leitura.

    Retorna:
    int: Valor digitado pelo usuário.

    Observação:
    Gera ValueError se o usuário digitar algo que não seja um número inteiro.
    '''
    print(msg)
    valor = int(input())
    return valor

def calcula_distancia(tempo, velocidade):
    '''
    Calcula a distância percorrida (distância = tempo x velocidade).

    Parâmetros:
    tempo (int): Tempo gasto na viagem, em horas.
    velocidade (int): Velocidade média, em km/h.

    Retorna:
    int: Distância percorrida, em km.
    '''
    return tempo * velocidade

def resultado(tempo, velocidade, distancia, litros):
    '''
    Mostra na tela o resumo da viagem.

    Parâmetros:
    tempo (int): Tempo gasto na viagem, em horas.
    velocidade (int): Velocidade média, em km/h.
    distancia (int): Distância percorrida, em km.
    litros (float): Combustível consumido, em litros.

    Retorna:
    None: A função apenas imprime os valores.
    '''
    print(f"Tempo: {tempo}")
    print(f"Velocidade: {velocidade}")
    print(f"Distancia: {distancia}")
    print(f"Litros: {litros}")

def calcula_litros(distancia):
    '''
    Calcula os litros de combustível gastos na viagem.

    Considera um consumo médio fixo de 12 km por litro.

    Parâmetros:
    distancia (int): Distância percorrida, em km.

    Retorna:
    float: Quantidade de litros consumidos.
    '''
    return distancia / 12

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    help(leitura)
    help(calcula_distancia)
    help(calcula_litros)
    help(resultado)
    tempo = leitura("Digite o Tempo Gasto na Viagem: ")
    velocidade = leitura("Digite o Limite da Velocidade: ")
    distancia = calcula_distancia(tempo, velocidade)
    litros = calcula_litros(distancia)
    resultado(tempo, velocidade, distancia, litros)
