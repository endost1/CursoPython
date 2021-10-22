# Exercício Python 106: 
# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
# Importante: use cores.

from time import sleep

def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{comando}\'', 4)
    print(cores[5], end='')
    help(com)
    print(cores[0], end='')
    sleep(1.5)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='') 
    print('-' * tamanho) 
    print(f'  {msg}')
    print('-' * tamanho)
    print(cores[0], end='') 
    sleep(1)


# Programa Principal #

cores = {0 : '\033[m',    # 0 - Limpo #
        1 : '\033[1;31m', # 1 - Vermelho #
        2 : '\033[1;32m', # 2 - Verde #
        3 : '\033[1;33m', # 3 - Amarelo #
        4 : '\033[1;34m', # 4 - Azul #
        5 : '\033[7;30m'  # 5 - Branco #
        };   

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 3)
    comando = str(input('Função ou Biblioteca [FIM encerra] > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
