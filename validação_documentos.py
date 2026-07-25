'''
Programa: validação_documentos.py
Descritivo: Bot de validação de documentos
'''
from valida_cpf import validar_cpf
from valida_cnpj import validar_cnpj


def validar_documento(tipo: str, documento: str) -> str:
    tipo = tipo.strip().lower()
    documento = documento.strip().upper()

    if tipo == "cpf":
        if validar_cpf(documento):
            return f"CPF '{documento}' válido."

        return f"CPF '{documento}' inválido."

    if tipo == "cnpj":
        if validar_cnpj(documento):
            return f"CNPJ '{documento}' válido."

        return f"CNPJ '{documento}' inválido."

    return "Tipo de documento desconhecido."


def bot() -> None:
    print("=" * 50)
    print("BOT DE VALIDAÇÃO DE DOCUMENTOS")
    print("=" * 50)

    while True:
        tipo = input(
            "\nQual documento deseja validar? "
            "(CPF, CNPJ ou SAIR): "
        ).strip()

        if tipo.lower() == "sair":
            print("Encerrando o bot...")
            break

        if tipo.lower() not in {"cpf", "cnpj"}:
            print("Opção inválida. Digite CPF, CNPJ ou SAIR.")
            continue

        documento = input(f"Digite o {tipo.upper()}: ")

        resultado = validar_documento(tipo, documento)
        print(resultado)


if __name__ == "__main__":
    bot()