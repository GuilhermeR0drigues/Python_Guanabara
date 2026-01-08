#import math
from math import hypot

cateto_oposto = int(input('Digite o valor do cateto oposto '))
cateto_adjacente = int(input('Digite o valor do cateto adjacente '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa é: {}'.format(hipotenusa))