'''
Programa para utilizar a biblioteca RANDOM
Gerar números aleatórios e realizar operações com a biblioteca RANDOM
'''
import random

# Gera um número aleatório entre 0 e 1
print(random.random())

# Gera um número aleatório inteiro entre 1 e 10
print(random.randint(1, 10))

# Gera um número aleatório a partir de uma lista
print(random.choice([1, 2, 3, 4, 5]))

# Gera um número aleatório dentro de um intervalo com passo específico
# apenas números pares dentro do intervalo 0 a 10. Se quiser números ímpares, altere o passo para 2 e o início para 1.
print(random.randrange(0, 10, 2)) 

# Gera uma amostra aleatória de 3 elementos a partir de uma lista
print(random.sample([1, 2, 3, 4, 5], 3))

# Embaralha a lista original
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

