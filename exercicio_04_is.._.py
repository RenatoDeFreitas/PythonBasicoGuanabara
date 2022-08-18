
""" o item é um objeto -
os itens que tem parêntese () são os métodos a strg tem métodos"""

nome = input('Qual seu nome?\n')

item = input(nome + ', por favor digite algo.\n')

print('O item digitado, {} é um tipo primitivo: '.format(item), type(item))
print()
print('Só tem espaço?', item.isspace())
print('O item {} é um número?'.format(item), item.isnumeric())
print('É alfabético.', item.isalpha())
print('{} é alfanumérico?'.format(item), item.isalnum())
print('Este item está em maiúsculo?', item.isupper())
print('Está em minúsculo?', item.islower())
print('{} está capitalizada?'.format(item), item.istitle())