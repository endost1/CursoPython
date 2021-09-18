# j = jogador, c = computador, t = tipo, n = número de jogada
from random import randint
from time import sleep
n = 0
print('-=' * 40)
while True:
    j = int(input('Digite um valor: '))
    c = randint(0, 10)
    total = j + c
    t = ' '
    while t not in 'PI':
        t = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
        print('UM')
        sleep(1)
        print('DOIS')
        sleep(1)
        print('TRÊS')
        sleep(1)
        print(f'O jogador digitou {j} e o computador digitou {c}. Total de {total}.', end=' ')
        print(f'Deu Par' if total % 2 == 0 else 'Deu Impar')
    if t == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            print('-=' * 40)
            n += 1
        else:
            print('Você PERDEU!')
            print('-=' * 40)
            print('Finalizando programa...')
            print('-=' * 40)
            sleep(1)
            break
    if t == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            print('-=' * 40)
            n += 1
        else:
            print('Você PERDEU!')
            print('-=' * 40)
            print('Finalizando programa...')
            print('-=' * 40)
            sleep(1)
            break
    print('Vamos continuar...')
    print('-=' * 40)
print(f'GAME OVER. você venceu {n} vezes.')