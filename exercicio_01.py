nome = input('Qual seu nome?\n')

print('Olá {}, é um prazer lhe conhecer!'.format(nome))
print()

p1 = int(input(nome + ', por favor, digite um número inteiro qualquer.\n'))

p2 = int(input('Agra digite outro número qualquer.\n'))
s = p1 + p2
print('A soma entre {} e {} é {}'.format(p1, p2, s))
