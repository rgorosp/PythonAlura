'''
Programa: lista_convidado_conjunto.py
Descrição: Adicione convidados à sua lista de aniversário. Como a lista é um
conjunto (set), nomes duplicados são ignorados automaticamente.
'''

convidados = set()

while True:
    nome = input('Digite o nome do convidado para seu aniversário: ').strip()

    if nome:
        if nome in convidados:
            print(f'"{nome}" já está na lista.')
        else:
            convidados.add(nome)

    flag = input('Deseja continuar? (s/n) ').strip().lower()
    if flag == 'n':
        break

print(f'\nTotal de convidados: {len(convidados)}')
for nome in sorted(convidados):
    print(f'- {nome}')
