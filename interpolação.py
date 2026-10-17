'''
Programa: interpolação.py
Descritivo: Trabalhando com interpolação de strings
'''
nome = "Emerson"
idade = 50 
cargo = "Especialista"
dados = {"nome": nome, "idade": idade, "cargo": cargo}

print("Meu nome é %s, tenho %d anos e meu cargo é %s" % (nome, idade, cargo))
print("Meu nome é {}, tenho {} anos e meu cargo é {}".format(nome, idade, cargo))
print(f"Meu nome é {nome}, tenho {idade} anos e meu cargo é {cargo}")
print("Meu nome é {nome}, tenho {idade} anos e meu cargo é {cargo}".format(nome=nome, idade=idade, cargo=cargo))
print("Meu nome é {0}, tenho {1} anos e meu cargo é {2}".format(nome, idade, cargo))
print("Meu nome é {nome}, tenho {idade} anos e meu cargo é {cargo}".format(**dados))
print(f"Meu nome é {dados['nome']}, tenho {dados['idade']} anos e meu cargo é {dados['cargo']}")
print("Meu nome é {nome}, tenho {idade} anos e meu cargo é {cargo}" % dados)