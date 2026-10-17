''' 
Programa: string_tipos.py
Descritivo. Trabalhando com Strings
''' 
nome = "Python"
texto = " Trabalhando com Strings   "
menu = "Emerson"
# Exibindo o nome em maiúsculas
print(nome.upper())
# Exibindo o nome em minúsculas
print(nome.lower())
# Exibindo o nome com a primeira letra maiúscula
print(nome.capitalize())
# Exibindo o texto sem espaços no início e no fim
print(texto.strip())
# Exibindo o texto sem espaços no início
print(texto.lstrip())
# Exibindo o texto sem espaços no fim
print(texto.rstrip())
# Formatando o Menu
print(menu.center(14, "#"))
# Unindo o menu com o caractere "-"
print("-".join(menu))