'''
Programa: lista_convidado_dicionario.py
Descrição: Adicione convidados à sua lista de aniversário. Usando a forma
de dicionário, guardando o número de acompanhantes de cada convidado.
'''

convidados = {}

while True:
    nome = input('Digite o nome do convidado para seu aniversário: ').strip()

    if nome:
        if nome in convidados:
            print(f'"{nome}" já está na lista.')
        else:
            acompanhantes = input(f'Quantos acompanhantes "{nome}" vai levar? ').strip()
            convidados[nome] = int(acompanhantes) if acompanhantes.isdigit() else 0

    flag = input('Deseja continuar? (s/n) ').strip().lower()
    if flag == 'n':
        break

total_pessoas = len(convidados) + sum(convidados.values())
print(f'\nConvidados na lista: {len(convidados)}')
print(f'Total de pessoas (com acompanhantes): {total_pessoas}')
for nome, acompanhantes in sorted(convidados.items()):
    print(f'- {nome} (+{acompanhantes})')
