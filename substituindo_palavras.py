'''
Programa: substituindo_palavras.py
Descritivo: Verifique a frase, e avalie se devemos alterar alguma palavra
da frase. Caso seja necessário, substitua a palavra e mostre a frase alterada. 
Caso não seja necessário, apenas mostre a frase original. 
'''
import os 

def processamento():
    frase = 'Meu nome é João e eu gosto de programar em Python.'
    flag = input(f"A frase é: '{frase}'\nDeseja alterar alguma palavra? (s/n): ").strip().lower()

    if flag == "s":
        palavra_antiga = input("Digite a palavra que deseja substituir: ").strip()
        palavra_nova = input("Digite a nova palavra: ").strip()
        if palavra_antiga in frase:
            frase_alterada = frase.replace(palavra_antiga, palavra_nova)
            print(f"Frase alterada: {frase_alterada}")
        else:
            print(f"A palavra '{palavra_antiga}' não foi encontrada na frase.")
            print(f"Frase original: {frase}")
    else:
        print("Nenhuma alteração será feita.")

def termino():
    print("\nProcessamento concluído. Obrigado por usar o programa.")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    processamento()
    termino()

if __name__ == "__main__":
    main()