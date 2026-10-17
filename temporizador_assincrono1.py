'''
Carlos é um engenheiro de software que precisa processar duas tarefas 
simultaneamente: uma que simula um download e outra que simula uma 
análise de dados. Ele quer que ambas as tarefas sejam iniciadas ao mesmo 
tempo, e que o programa exiba mensagens informando o início e o fim de 
cada uma.
'''
import asyncio  # Biblioteca para programação assíncrona
async def download():
    print("Iniciando download...")
    await asyncio.sleep(3)  # Simula o tempo de download
    print("Download concluído!")

async def analise_dados():
    print("Iniciando análise de dados...")
    await asyncio.sleep(5)  # Simula o tempo de análise de dados
    print("Análise de dados concluída!")

# Executando ambas as tarefas simultaneamente
async def main():
    await asyncio.gather(download(), analise_dados())

asyncio.run(main())