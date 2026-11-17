'''
Média escolar
'''
import os

def leitura(fmedia):
    calculo = 0
    for i in range(1, 6):
        os.system('cls' if os.name == 'nt' else 'clear')
        nota = float(input(f"Digite a {i} nota: "))
        calculo = calculo + nota
    media = calculo / 5
    media = round(media, 2)
    return media
        
if __name__ == "__main__":
        fmedia = leitura(fmedia=0)
        if (fmedia >= 0.0 and fmedia <= 4.0):
            print(f"O aluno está reprovado, nota final {fmedia}")
        elif fmedia > 4.0 and fmedia <= 6.0:
            print(f"O aluno está de recuperação! Nota final {fmedia}")
        else:
            print(f"O aluno está aprovado! Nota final {fmedia}")
