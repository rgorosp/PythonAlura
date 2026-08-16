"""
TESTE
"""
lista = ['Emerson', 'Leila', 'Livia']

print(lista)
print('O que deseja fazer? (a)lterar nome, (r)emover último nome, (n)ada')
entrada = input()
if entrada == 'a':
    nome = input('Digite o nome a ser alterado: ')
    if nome in lista:
        novo_nome = input('Digite o novo nome: ')
        indice = lista.index(nome)
        lista[indice] = novo_nome
        print(f'Nome alterado. Lista atual: {lista}')
    else:
        print("Nome não existe!!!")
elif entrada == 'r':
    if lista:
        removido = lista.pop()
        print(f'{removido} removido. Lista atual: {lista}')
    else:
        print("Lista já está vazia!!!")
else:
    exit()
