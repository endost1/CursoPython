#add cores
n1 = int(input('Digite um número:'))
s = n1 + 1
a = n1 - 1

cores = {'limpo':'\033[m',
        'vermelho.n':'\033[1;31m',
        'verde.n':'\033[1;32m',
        'amarelo.n':'\033[1;33m' }

print('O sucessor de {}{}{} é {}{}{}'.format(cores['amarelo.n'], n1, cores['limpo'], cores['verde.n'], s, cores['limpo']))
print('e o antecessor de {}{}{} é {}{}{}!'.format(cores['amarelo.n'], n1, cores['limpo'], cores['vermelho.n'], a, cores['limpo']))