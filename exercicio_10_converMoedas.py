
carteira = float(input('Quanto tem em sua carteira?\nR$ '))
dolar = float(input('Qual a cotação do dolar hoje?\nU$ '))

compraDolar = carteira / dolar

print('Com R$ {:.2f} e o dolar cotado a U$ {:.2f} você conseguiria compar U$ {:.2f}'.format(carteira, dolar, compraDolar))


