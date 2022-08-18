
nome = str(input('Digite seu nome completo.\n')).strip()
procura = str(input('Qual o nome procurado?\n')).strip()

print(f'A palavra {procura.lower()} tem no nome? {procura.lower() in nome.lower()}')
