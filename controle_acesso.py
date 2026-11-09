'''
Programa de controle de acesso baseado no horário do sistema.
'''
import os
from datetime import datetime

def receba_hora_sistema():
    hora_atual = datetime.now().strftime("%H:%M:%S")
    print(f"Hora atual do sistema: {hora_atual}")

def define_hora_atual(mensagem):
    hora_digitada = input(mensagem)

    if (hora_digitada > "08:00:00" and hora_digitada < "18:00:00"):
        print("Dentro do horário comercial, horário permitido para acesso.")
    else:
        print("Fora do horário comercial, acesso não permitido.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    receba_hora_sistema()
    define_hora_atual("Digite a Hora atual: ")
