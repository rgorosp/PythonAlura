#Programa: main.py
#Programador: Emerson S Motta
#Data: 20/03/2024
#Descrição: Programa que utiliza a API da OpenAI para responder perguntas sobre Python.
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") ## Carrega a chave da API do arquivo .env

client = OpenAI(api_key=api_key) ## Cria o cliente da API da OpenAI com a chave carregada

resposta = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[
        {"role": "system", "content": "Você é um assistente que ajuda em Python."},
        {"role": "user", "content": "Me explique o que é JCL no mainframe."}
    ]
)

print(resposta.choices[0].message.content)