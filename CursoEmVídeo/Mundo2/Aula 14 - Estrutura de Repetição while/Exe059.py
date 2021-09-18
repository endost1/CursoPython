'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''           [ 1 ] somar
           [ 2 ] multiplicar
           [ 3 ] maior
           [ 4 ] novos valores
           [ 5 ] finalizar programa''')
    op = int(input('Qual a sua opção? '))
    if op == 1:
        s = n1 + n2
        print(f'O resultado da soma {n1} + {n2} é {s}')
    elif op == 2:
        m = n1 * n2
        print(f'O resultado da multiplicação {n1} * {n2} é {m}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif op == 4:
        print('Informe os novos números:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundp número: '))
    elif op == 5:
        print('Finalizando o programa...')
    else:
        print('Informação invalidade. Tente novamente!')
    print('-=' * 20)
    sleep(1)
print('Programa finalizado!')