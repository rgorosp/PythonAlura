'''
Programa: pacientes.py
Descritivo: O programa, recebe informações de pacientes de um Hospital,
no formato: "PrimeiroNome Sobrenome - Ano". A idéia é capturar cada parte
separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema. 
'''
import re,os
from datetime import date

programa = 'pacientes.py'
dados = ''

# Processamento do programa
def processamento() -> None:
    dados = input('Digite o nome completo e o ano de nascimento do paciente: ').strip()

    padrao = (
        r"(?P<primeiro_nome>[^\W\d_]+)\s+"
        r"(?P<sobrenome>[^\W\d_]+)\s*-\s*"
        r"(?P<ano>\d{4})"
    )

    resultado = re.fullmatch(padrao, dados)

    data = date.today()

    print(resultado)

    if resultado is None:
        print('Dados Inválidos!!!')
        return
    else:
        primeiro_nome = resultado.group('primeiro_nome')
        sobrenome = resultado.group('sobrenome')
        ano = resultado.group('ano')

        print('-' *34)
        print('         P A C I E N T E')
        print('----------------------------------')
        print(f'Nome......: {primeiro_nome}')
        print(f'Sobrenome.: {sobrenome}')
        print(f'Nascimento: {ano}')
        print(f'Data Hoje.: {data}')
        print('----------------------------------')
      
# Termino do Programa
def termino():
    print(f'\nTermino do Programa: {programa}\n')
    os._exit(0)

# Inicio do Programa
def main():
    os.system("cls" if os.name == "nt" else "clear")
    processamento()
    termino()

if __name__ == "__main__":
    main()