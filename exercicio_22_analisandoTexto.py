
nome = str(input('Digite seu nome completo.\n')).strip()

print('Seu nome em maiúsculo é', nome.upper())
print('Em minúsculo é', nome.lower())
print('Tem o total de {} letras'.format(len(nome) - nome.count(' ')))
# print('o primeiro nome tem {} letras.'.format(nome.find(' ')))
separado = nome.split() # separa e coloca em uma lista
print('O pimeiro nome é {} e tem {} letras'.format(separado[0], len(separado[0])))