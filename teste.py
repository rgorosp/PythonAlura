"""
TESTE
"""
import os 
tupla1 = ('Emerson',50,1.75)
tupla2 = ('Livia',18,1.65)
tupla3 = ('Leila',44,1.60)

lista = [tupla1, tupla2, tupla3]

for tupla in lista:
    nome, idade, altura = tupla
    print(f'Nome: {nome} - Idade: {idade} - Altura: {altura}')

print('\nTermino do Teste de Programa')
os._exit(0)