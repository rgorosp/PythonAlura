'''
Programa para utilizar a biblioteca TIME
'''
import time as tm

# Obtém o tempo atual em segundos desde a época (1 de janeiro de 1970)
print(tm.time())

# Pausa a execução do programa por 2 segundos
tm.sleep(2)

# Obtém a hora local atual
print(tm.localtime())

# Mede o tempo decorrido para executar um loop vazio
antes = tm.time()
for t in range(10000):
    pass
depois = tm.time()
print("Tempo decorrido:", depois - antes, 'segundos')

# Formata a hora local atual como uma string legível
print(tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime()))

# Obtém a hora UTC atual
print(tm.gmtime())

# Formata a hora UTC atual como uma string legível
print(tm.strftime("%Y-%m-%d %H:%M:%S", tm.gmtime()))

# Converte uma string de data e hora para um objeto struct_time
date_string = "2024-06-15 12:34:56"
print(tm.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
