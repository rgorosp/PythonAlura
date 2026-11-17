'''
Exemplo de iteração sobre uma tupla com índice
'''
import os

tuplas = (1, 2, 3, 4, 5)

os.system('cls' if os.name == 'nt' else 'clear')
for i, item in enumerate(tuplas):
    print(f'Index {i}: {item}')



