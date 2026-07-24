'''
Programa: validação_site.py
Descrição: Validar se o site corresponde com os padrões de entrada.
O mesmo deve iniciar com http:// ou https:// e deve terminar com .com, 
.org, .edu, .gov, .net ou .br. 
'''
import os 

# processamento do programa
def processamento():
    controle = True
    while controle:
        try:
            site = input("Digite o site: ").strip()
            if (site.startswith("http://") or site.startswith("https://")) and \
               (site.endswith(".com") or site.endswith(".org") or site.endswith(".edu") or \
                site.endswith(".gov") or site.endswith(".net") or site.endswith(".br")):
                print(f"O site '{site}' é válido.")
                controle = False
            else:
                print(f"O site '{site}' é inválido.")
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada interrompida. Encerrando a validação.")
            controle = False

# Termino do programa
def termino():
    print("\nValidação concluída. Obrigado por usar o programa.")

# Inicio do programa
def main(): 
    os.system("cls" if os.name == "nt" else "clear")
    processamento() 
    termino()

if __name__ == "__main__":
    main()


