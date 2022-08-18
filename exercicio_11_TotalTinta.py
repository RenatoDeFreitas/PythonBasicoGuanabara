
largura = float(input('Digite a largura da parede.\nm² '))
altura = float(input('Digite a altura da parede.\n'))
area = largura * altura
tinta_necessária = area / 2
print('A parede mede {:.2f} largura X {:.2f} altura possuindo o total de {:.2f}m².'.format(largura, altura,area))
print('São necessários {:.2f} litros de tinta para pintar {:.2f}m²'.format(tinta_necessária, area))


