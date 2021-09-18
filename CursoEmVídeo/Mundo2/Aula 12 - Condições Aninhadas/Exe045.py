# Crie um programa que faça o computador jogar Jokenpô com você:
from random import randint
from time import sleep
print(f'{"JOKENPÔ":=^40}')
print('''
[ 1 ]: PEDRA
[ 2 ]: PAPEL
[ 3 ]: TESOURA''')
jogador = int(input('Qual a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('JO!')
sleep(1)
print('KEN!!')
sleep(1)
print('PÔ!!!')
print('-=' * 10)
print(f'O jogador escolheu {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
print('-=' * 10)
if jogador == 1: # jogador jogou PEDRA
    if computador == 1:
        print('Computador ganhou!')
    elif computador == 2:
        print('Jogador ganhou')
    else:
        print('Empate!')
elif jogador == 2: # jogador jogou PAPEL
    if computador == 0:
        print('Jogador ganhou!')
    elif computador == 2:
        print('Computador ganhou!')
    else:
        print('Empate!')
elif jogador == 3: # jogador jogou TESOURA
    if computador == 0:
        print('Computador ganhou!')
    elif computador == 1:
        print('Jogador ganhou!')
    else:
        print('Empate!')