'''
Programa: decifrando_pistas.py
Descritivo: Tente decifrar qual a palavra escondida na frase. 
A palavra é formada pelas letras maiúsculas da frase.
'''
import os

frase = 'Misterioso'
frase_inicio = frase[:3]
frase_final = frase[-3:]

def processamento():
    texto = f'A palavra escondida na frase é: {frase_inicio} ... {frase_final}'
    print(texto)
    escreva = input(f'\nDigite a palavra escondida: ')
    contador = 0
    while contador < 3:

        if escreva == frase:
            print(f'\nParabéns! Você acertou a palavra escondida: {frase}')
            break
        else:
            contador += 1
            print(f'\nVocê errou! Tente novamente. Tentativa {contador} de 3.')
            escreva = input(f'Digite a palavra escondida: ')
            if contador == 3:
                print(f'\nSuas tentativas acabaram! A palavra correta era: {frase}')

def termino():
    print("\nFim do Programa")

def main():
    os.system('cls')
    processamento() 
    termino()





if __name__ == "__main__":
    main()