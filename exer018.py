import math

angulo = int(input('Digite o valor do angulo '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))
