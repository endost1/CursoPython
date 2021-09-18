# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
from time import sleep
print('PA, usando while')
print('-=' * 20)
num = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = num + (10 - 1) * r
n = num
c = 1
print('-=' * 20)
print('Calculando...')
sleep(2)
while c <= 10:
    print(f'{n} → ', end='')
    n += r
    c += 1
print('Fim')