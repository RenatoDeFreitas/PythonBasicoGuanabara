
frase = str(input('Digite uma frase qualquer.\n').lower()).strip()
letra = str(input('Qual a letra a ser analisada.\n').lower()).strip()
procura = frase.find(letra) + 1

print(f'A letra +{letra}+ aparece {frase.count(letra.lower())} vezes.')
print(f'A letra +{letra}+ aparece a primeira vez na posição {frase.find(letra) + 1}')
print(f'A última aparição da letra +{letra}+ foi na posição {frase.rfind(letra) + 1} ')