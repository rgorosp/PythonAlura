'''
Programa para chamar funções da biblioteca criada pelo usuário
'''
import os
import bibl_minha as bm

def documento():
    """Solicita três números e usa a biblioteca bibl_minha para somá-los.

    Args:
        texto: Mensagem exibida antes da solicitação dos números.

    Returns:
        Resultado da soma calculada por ``bm.somar``.
        Resultado da subtração calculada por ``bm.subtrair``.
        Resultado da multiplicação calculada por ``bm.multiplicar``.
        Resultado da divisão calculada por ``bm.dividir``.
    """

# Função para solicitar três números e somá-los usando a biblioteca bibl_minha
def somar(texto):
    print(texto)
    numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(3)]
    return bm.somar(*numeros)

help(documento)
input("Pressione Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')
resultado = somar("Digite os números para somar: ")
print(resultado)