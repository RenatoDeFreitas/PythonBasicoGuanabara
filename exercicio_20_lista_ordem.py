import random

n1 = input('Nome 01: ')
n2 = input('Nome 02: ')
n3 = input('Nome 03: ')
n4 = input('Nome 04: ')
lista = [n1, n2, n3, n4]

print(f'A lista original era {lista}')

random.shuffle(lista)
print('Lista embaralhada é')

print(lista)



