# Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário. 
# Programa: procura_chave.py
import os
dados = {
    'Nome': 'Maria',
    'Idade': 25,
    'Cidade': 'Rio de Janeiro',
    'Profissão': 'Designer'
}

# FUNÇÃO PARA PROCURAR A CHAVE NO DICIONÁRIO
def procurar_chave(chave):
    if chave in dados:
        print(f"A chave '{chave}' existe no dicionário. Valor: {dados[chave]}")
    else:
        print(f"A chave '{chave}' não existe no dicionário.")

    continuar = input("Deseja procurar outra chave? (s/n): ").lower()
    if continuar == 's':
        nova_chave = input("Digite a nova chave que deseja procurar: ")
        procurar_chave(nova_chave)
    else:
        print("Encerrando o programa. Obrigado por usar!")

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    chave_a_procurar = input("Digite a chave que deseja procurar: ")
    procurar_chave(chave_a_procurar)

if __name__ == "__main__":
    main()