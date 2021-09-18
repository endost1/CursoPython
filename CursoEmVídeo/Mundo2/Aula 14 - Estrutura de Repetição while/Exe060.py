'''def main()
from math import factorial
n = int(input('Digite um valor inteira para saber seu fatorial: ))
f = factorial(n)
print(f'{n}! é igual á {f}')'''
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
from time import sleep
n = int(input('Digite um valor inteiro para saber seu fatorial: '))
i = n
n_f = 1
print('Calculando...')
sleep(2)
print(f'{n}! = ', end='')
while i > 0:
    print(f'{i}', end='')
    print(f' * ' if i > 1 else ' = ', end='')
    n_f *= i
    i -= 1
print(f'{n_f}')
print('-=' * 20)
sleep(2)
print('Finalizando...')
print('-=' * 20)
sleep(2)
print('Fim do programa!')
