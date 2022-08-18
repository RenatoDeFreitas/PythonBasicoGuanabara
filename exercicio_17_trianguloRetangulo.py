import math
co = float(input('Valor catato oposto. '))
ca = float(input('Valor cateto adjacente. '))

# hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
hipotenusa = math.hypot(co, ca)
print('Cateto oposto {} e cateto adjacente {}\n Hipotenusa é {:.2f}.'.format(co, ca, hipotenusa))