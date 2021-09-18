nu = int(input('Digite um número de 0 a 9999: '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print('uniddade {}.'.format(u))
print('dezena {}.'.format(d))
print('centena {}.'.format(c))
print('milhar {}.'.format(m))
