'''
Programa: valida_cnpj.py

Descritivo:
O programa valida o formato e os dígitos verificadores de um CNPJ
numérico ou alfanumérico.

Formato esperado:

AA.AAA.AAA/AAAA-00

As 12 primeiras posições podem conter letras maiúsculas e números.
As duas últimas posições são os dígitos verificadores e permanecem
exclusivamente numéricas.

O programa utiliza REGEX para validar o formato e o algoritmo de
módulo 11 para validar os dígitos verificadores.
'''

import os
import re


# Pesos utilizados no cálculo dos dígitos verificadores
PESOS_PRIMEIRO_DIGITO = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

PESOS_SEGUNDO_DIGITO = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def validar_formato_cnpj(cnpj: str) -> bool:
    """
    Valida somente o formato do CNPJ.

    Exemplos aceitos:
        12.345.678/0001-95
        AB.CDE.FG1/23H4-32
    """

    padrao = (
        r"[A-Z0-9]{2}\."
        r"[A-Z0-9]{3}\."
        r"[A-Z0-9]{3}/"
        r"[A-Z0-9]{4}-"
        r"\d{2}"
    )

    return re.fullmatch(padrao, cnpj) is not None


def remover_mascara(cnpj: str) -> str:
    """
    Remove os pontos, a barra e o hífen do CNPJ.
    """

    return re.sub(r"[./-]", "", cnpj)


def converter_caractere(caractere: str) -> int:
    """
    Converte um número ou uma letra para o valor usado
    no cálculo dos dígitos verificadores.

    Exemplos:
        0 -> 0
        9 -> 9
        A -> 17
        B -> 18
        Z -> 42
    """

    return ord(caractere) - 48


def calcular_digito(base: str, pesos: tuple[int, ...]) -> int:
    """
    Calcula um dígito verificador do CNPJ.
    """

    soma = sum(
        converter_caractere(caractere) * peso
        for caractere, peso in zip(base, pesos)
    )

    resto = soma % 11

    if resto < 2:
        return 0

    return 11 - resto


def validar_digitos_cnpj(cnpj: str) -> bool:
    """
    Valida os dois dígitos verificadores do CNPJ.
    """

    cnpj_sem_mascara = remover_mascara(cnpj)

    # O CNPJ deve possuir 14 posições
    if len(cnpj_sem_mascara) != 14:
        return False

    # As 12 primeiras posições formam a base
    base = cnpj_sem_mascara[:12]

    # As duas últimas posições são os dígitos verificadores
    digitos_informados = cnpj_sem_mascara[12:]

    # Segurança adicional: os dígitos verificadores devem ser numéricos
    if not digitos_informados.isdigit():
        return False

    primeiro_digito = calcular_digito(
        base,
        PESOS_PRIMEIRO_DIGITO
    )

    segundo_digito = calcular_digito(
        base + str(primeiro_digito),
        PESOS_SEGUNDO_DIGITO
    )

    digitos_calculados = f"{primeiro_digito}{segundo_digito}"

    return digitos_informados == digitos_calculados


def validar_cnpj(cnpj: str) -> bool:
    """
    Valida o formato e os dígitos verificadores.
    """

    cnpj = cnpj.strip().upper()

    return (
        validar_formato_cnpj(cnpj)
        and validar_digitos_cnpj(cnpj)
    )


def processamento() -> None:
    """
    Solicita e valida os CNPJs digitados pelo usuário.
    """

    while True:
        cnpj = input(
            "Digite o CNPJ da empresa "
            "(ou 'sair' para encerrar): "
        ).strip()

        if cnpj.lower() == "sair":
            break

        # Padroniza as letras como maiúsculas
        cnpj = cnpj.upper()

        if not validar_formato_cnpj(cnpj):
            print(
                "Erro: use o formato "
                "AA.AAA.AAA/AAAA-00."
            )

        elif not validar_digitos_cnpj(cnpj):
            print(
                f"Erro: os dígitos verificadores "
                f"do CNPJ '{cnpj}' são inválidos."
            )

        else:
            print(f"CNPJ '{cnpj}' válido.")


def termino() -> None:
    """
    Exibe a mensagem final do programa.
    """

    print("Encerrando o programa...")
    os._exit(0)


def main() -> None:
    """
    Função principal do programa.
    """

    os.system("cls" if os.name == "nt" else "clear")

    processamento()
    termino()


if __name__ == "__main__":
    main()