"""
Programa..: cafeteria.py
Author....: Emerson S Motta
Descritivo: Esse programa calcula quantidade de itens recebidos, e aplica
10% para clientes cadastrados na Loja
"""
import os

qtdPedidos = 0

# PROCESSAMENTO DOS DADOS
def processamento():
   total = 0.0
   qtdPedidos = int(input("Qual a quantidade de Itens para esse pedido: ? \n"))

   if qtdPedidos == 0:
      print("Não há pedidos, Tenha um Bom dia!")
   else:
      for i in range(1, qtdPedidos + 1):
         item = input(f"Qual o {i} item ? ")
         valor = float(input("Digite o Valor $ " ))
         total = total + valor
         print("")

   flag = input("Você possui cadastro na Loja ? <S> ou <N> ").strip().upper()

   if flag == 'S':
      desconto = total * 0.10
      total = total - desconto

   print(f"Total do Pedido a Pagar ${total}")

   print("\nFim do Programa")

# INICIO DO PROGRAMA PRINCIPAL
def main():
      os.system('cls' if os.name == 'nt' else 'clear')
      processamento()

if __name__ == "__main__":
      main()



