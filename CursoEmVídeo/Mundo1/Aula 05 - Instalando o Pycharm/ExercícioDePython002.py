#add cores
n = input('Digite seu nome:')
cores = {'limpo':'\033[m',
        'vermelho.n':'\033[1;31m',
        'verde.n':'\033[1;32m',
        'amarelo.n':'\033[1;33m',
        'azul.n':'\033[1;34m' }
print('Prazer em te conhecer, {}{}{}!'.format(cores['amarelo.n'], n, cores['limpo']))
