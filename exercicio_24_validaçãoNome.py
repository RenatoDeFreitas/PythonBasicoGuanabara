
cidade = str(input('Qual cidade você nasceu?\n')).strip()
validação = str(input('qual a palavra a ser validada?\n')).strip()

cid_lista = cidade.split()[0].capitalize()

print(f'O primeiro nome da cidade é {cid_lista}')
print(cid_lista == validação.capitalize())
