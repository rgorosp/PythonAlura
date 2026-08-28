'''
Programa: registro_alunos.py
Descritivo: Lê nome, idade e nota de vários alunos e gera um relatório.
'''

alunos = []

while True:
    entrada = input("Digite Nome, Idade e Nota (separados por vírgula): ").strip()

    try:
        nome, idade, nota = [campo.strip() for campo in entrada.split(",")]
        aluno = {
            "nome": nome,
            "idade": int(idade),
            "nota": float(nota.replace(",", ".")),
        }
    except ValueError:
        print("Entrada inválida. Use o formato: João, 20, 8.5")
        continue

    alunos.append(aluno)

    if input("Deseja continuar? (s/n): ").strip().lower() != "s":
        break

# Relatório
print("\n" + "=" * 40)
print(f"{'NOME':<20}{'IDADE':<8}{'NOTA':<6}")
print("-" * 40)
for a in alunos:
    print(f"{a['nome']:<20}{a['idade']:<8}{a['nota']:<6.1f}")
print("=" * 40)
print(f"Total de alunos: {len(alunos)}")

if alunos:
    media = sum(a["nota"] for a in alunos) / len(alunos)
    print(f"Média da turma: {media:.2f}")
