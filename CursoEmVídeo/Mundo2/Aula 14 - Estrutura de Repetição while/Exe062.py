# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
from time import sleep
print('PA, usando while')
print('-=' * 20)
num = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = num + (10 - 1) * r
n = num
c = 1
t = 0
m = 10
print('-=' * 20)
print('Calculando...')
sleep(2)
while m != 0:
    t += m
    while c <= t:
        print(f'{n} → ', end='')
        n += r
        c += 1
    print('Pausa')
    m = int(input('Quer adicionar quantos termos a mais? '))
    print('-=' * 20)
    print('Calculando...')
    sleep(2)
    if m == 0:
        print('-=' * 20)
        print('Finalizando... ', end='')
        sleep(2)
print('Fim')
print('-=' * 20)
print(f'Progressão finalizada com {t} termos contados!')
