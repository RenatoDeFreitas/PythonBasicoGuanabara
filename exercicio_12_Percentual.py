
preco = float(input('Qual o preço do produto? R$ '))
desconto = float(input('Qual o desconto pretende dar? '))
desReal = desconto / 100
precoDescontado = preco + (preco * desReal)
print('Com o preço de R$ {} com o desconto de {}%.'.format(preco, desconto))
print('O valor de {} % corresponde a R$ {:.2f}'.format(desconto, preco * desReal))
print('O valor com desconto do produto é R$ {:.2f}'.format(precoDescontado))