'''
Programa: valida_cpf.py
Descritivo: O formato esperado do CPF é: três blocos de 3 dígitos 
separados por pontos (.), seguidos por um bloco de 2 dígitos separados 
por um traço (-). Importante: Hoje o CPF pode conter letras e numeros.
IMPORTANTE: O programa usa o REGEX para validar o CPF e exibe uma mensagem de erro
caso o CPF não esteja no padrão esperado. 
'''
import os 
import re

def validar_cpf(cpf):
    # Expressão regular para validar o formato do CPF
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(padrao, cpf) is not None

def validar_digitos(cpf):
    # Remove os caracteres não numéricos do CPF
    cpf_numeros = re.sub(r'\D', '', cpf)

    # Verifica se o CPF tem 11 dígitos
    if len(cpf_numeros) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf_numeros == cpf_numeros[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf_numeros[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf_numeros[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10

    # Verifica se os dígitos verificadores estão corretos
    return (int(cpf_numeros[9]) == primeiro_digito and
            int(cpf_numeros[10]) == segundo_digito)

def processamento():
    while True:
        cpf = input("Digite o CPF do cliente (ou 'sair' para encerrar): ")

        if cpf.lower() == "sair":
            break

        valido = validar_cpf(cpf)
        if valido:
            valido = validar_digitos(cpf)
            if valido:
                print(f"CPF '{cpf}' válido.")
            else:
                print("Erro: O CPF é inválido.")
        else:
            print("Erro: O CPF deve estar no formato 999.999.999-99.")

def termino():
    print("Encerrando o programa...")
    os._exit(0)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    processamento()
    termino()

if __name__ == "__main__":
    main()