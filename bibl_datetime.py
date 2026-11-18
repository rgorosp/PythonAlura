'''
Programa para utilizar a biblioteca DATETIME
'''
import datetime

print("-" * 50)  # Separar os comandos abaixo
print(f"Tipos da biblioteca datetime:\n" + "\n".join(dir(datetime)))
print("-" * 50)  # Separar os comandos abaixo
# Imprime a data e hora atual
print(datetime.datetime.now())
# Imprime apenas a data atual
print(datetime.date.today())
# Cria uma data específica
print(datetime.date(2024,6,10))
# Cria um horário específico
print(datetime.time(14,30,0))
# Cria um objeto datetime específico
print(datetime.datetime(2024,6,10,14,30,0))
# Formata a data e hora atual como string
print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
# Formata apenas a data atual como string
print(datetime.date.today().strftime("%d/%m/%Y"))
# Formata apenas a hora atual como string
print(datetime.datetime.now().strftime("%H:%M:%S"))
# Cria um objeto datetime a partir de uma string
print(datetime.datetime.strptime("10/06/2024 14:30:00", "%d/%m/%Y %H:%M:%S"))
# Cria um objeto date a partir de uma string
print(datetime.datetime.strptime("10/06/2024", "%d/%m/%Y").date())
