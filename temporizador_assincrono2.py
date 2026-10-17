'''
Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. 
Como cálculos pesados podem demorar, ele quer garantir que todos sejam 
processados ao mesmo tempo, e os resultados exibidos assim que estiverem prontos.
Crie um programa que calcule o fatorial de cinco números diferentes de forma 
assíncrona, onde os cálculos devem ser realizados paralelamente e exiba os 
resultados conforme forem concluídos, em ordem de menor número para maior número.
Dica: use a função sleep para simular um tempo de processamento.
Dica: para testar o funcionamento do seu código, utilize uma lista de números 
em ordem de tamanho aleatória. Exemplo: numeros = [5, 3, 7, 4, 6]
'''
import asyncio # Biblioteca para programação assíncrona
import random  # Biblioteca para gerar números aleatórios

async def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        await asyncio.sleep(0.1)  # Simula tempo de processamento
    return n, resultado

async def main():
    numeros = [5, 3, 7, 4, 6]
    tarefas = [fatorial(n) for n in numeros]
    resultados = await asyncio.gather(*tarefas)
    for n, resultado in sorted(resultados):
        print(f"Fatorial de {n} é {resultado}")

asyncio.run(main())
