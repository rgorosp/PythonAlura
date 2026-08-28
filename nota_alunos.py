'''
Programa: nota_alunos.py
Descrição: Recebe as 4 notas do aluno, mostra a média e diz se foi
aprovado, reprovado ou ficou de recuperação.
'''

import os

def ler_nota(ordem):
    while True:
        try:
            nota = float(input(f"Digite a {ordem} nota: ").replace(",", "."))
        except ValueError:
            print("  Valor inválido. Use números, ex: 7.5")
            continue
        if 0 <= nota <= 10:
            return nota
        print("  A nota deve estar entre 0 e 10.")


def processamento():
    nome = input("Digite seu nome: ")
    materia = input("Digite a matéria: ")
    notas = [ler_nota(o) for o in ("primeira", "segunda", "terceira", "quarta")]

    media = sum(notas) / len(notas)

    if media < 5:
        situacao, incentivo = "foi Reprovado", "não desista!"
    elif media >= 7:
        situacao, incentivo = "foi Aprovado", "parabéns!"
    else:
        situacao, incentivo = "esta de Recuperação", "continue estudando!"

    return (
        f"\n{nome}, sua média em {materia} foi {media:.2f}.\n"
        f"Você {situacao} — {incentivo}"
    )


def main():
    os.system("cls" if os.name == "nt" else "clear")
    mensagem = processamento()
    print(mensagem)
    print("\nTérmino do programa")


if __name__ == "__main__":
    main()
