#Programa: main.py
#Programador: Emerson S Motta
#Data: 20/03/2024
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um assistente que ajuda em Python."},
        {"role": "user", "content": "Me explique o que é JCL no mainframe."}
    ]
)

print(resposta.choices[0].message.content)