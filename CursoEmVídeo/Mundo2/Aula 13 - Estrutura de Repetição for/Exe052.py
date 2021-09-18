# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número inteiro: '))
d = 0
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[33m', end=' ')
        d += 1
    else:
        print('\033[31m', end=' ')
    print(f'{n}', end=' ')
print(f'\n\033[mO número {num} foi disivel {d} vezes.')
if d == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')
print('-=' * 20)
print('FIM DO ALGORITMO')