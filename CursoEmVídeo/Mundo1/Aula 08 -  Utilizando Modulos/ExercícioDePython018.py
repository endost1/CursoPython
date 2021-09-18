from math import radians, sin, cos, tan
a = int(input('Digite o ângulo que deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O valor do Seno do ângulo é {:.2f}'.format(s))
print('O valor do Cosseno do ângulo é {:.2f}'.format(c))
print('O valor da Tangente do ângulo é {:.2f}'.format(t))

"""import math
a = int(input('Digite o ângulo que deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O valor do Seno do ângulo é {:.2f}'.format(s))
print('O valor do Cosseno do ângulo é {:.2f}'.format(c))
print('O valor da Tangente do ângulo é {:.2f}'.format(t))"""
