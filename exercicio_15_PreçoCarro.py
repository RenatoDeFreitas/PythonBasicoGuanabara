
km_percorrido = int(input('Quantos Km foram percorrido? '))
dias_alugados = float(input('Quantos dias de aluguel? '))
v_total = dias_alugados * 60 + km_percorrido * 0.15

print('Para {} dias de aluguel você pagará R${}'.format(dias_alugados, dias_alugados * 60))
print('O Km rodade é R$ 0,15.\nPara {} Km você pagará o total de R$ {}.'.format(km_percorrido, km_percorrido * 0.15))
print('O valor total a ser pago é R$ {:.2f}'.format(v_total))