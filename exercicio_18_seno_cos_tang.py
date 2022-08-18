import math

angulo = float(input('Digite o ângulo!\n'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))

print(' Para o ângulo de {}°, o seno = {:.2f} e cosseno = {:.2f}'.format(angulo, seno, cosseno))

