'''
Criando um temporizador assíncrono usando a biblioteca asyncio do Python.
Neste exemplo, há apenas um temporizador, então ele simplesmente espera cinco 
segundos. O benefício da abordagem assíncrona aparece quando o programa precisa
fazer outras tarefas enquanto aguarda — por exemplo, executar vários 
temporizadores ao mesmo tempo.
'''
import asyncio  # Biblioteca para programação assíncrona

async def temporizador(segundos):
    print(f"Iniciando temporizador de {segundos} segundos...")
    await asyncio.sleep(segundos)
    print("Tempo esgotado!")

# Executando o temporizador assíncrono
asyncio.run(temporizador(5))
