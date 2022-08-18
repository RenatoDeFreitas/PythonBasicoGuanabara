print('exer.08')
metro = float(input('Digite o valor do m²? '))
print('O valor de {} m² em centímetro é {} e em milímetro é {}'.format(metro, metro * 100, metro * 1000))

print('{} Km, {} Hm, {} Dam'.format(metro / 1000, metro / 100, metro / 10))
print('{}Dm, {}Cm, {}mm'.format(metro*10, metro*100, metro*1000))