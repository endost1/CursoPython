from math import hypot
print('Áfim de encontrar a hipotenusa do triângulo retangulo?')
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
h = hypot (c1, c2)
print('A hipotenusa é igual a {:.2f}!'.format(h))

"""import math
print('Áfim de encontrar a hipotenusa do triângulo retangulo?')
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(c1, c2)
print('A hipotenusa é igual a {:.2f}!'.format(h))"""

"""print('Áfim de encontrar a hipotenusa do triângulo retangulo?')
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
h = (c1**2 + c2**2)**(1 / 2)
print('A hipotenusa é igual a {:.2f}!'.format(h))"""
