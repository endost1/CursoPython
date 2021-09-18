#add cores
n1 = int(input('Digite um número:'))
d = n1 * 2
t = n1 * 3
r = n1 ** 0.5

cores = {'limpo':'\033[m',
        'vermelho.n':'\033[1;31m',
        'verde.n':'\033[1;32m',
        'amarelo.n':'\033[1;33m',
        'azul.n':'\033[1;34m'}

print('o \033[1;36mdobro\033[m de {}{}{} é {}{}{};'.format(cores['amarelo.n'], n1, cores['limpo'], cores['vermelho.n'], d, cores['limpo']))
print('o \033[1;36mtriplo\033[m de {}{}{} é {}{}{};'.format(cores['amarelo.n'], n1, cores['limpo'], cores['verde.n'], t, cores['limpo']))
print('e a \033[1;36mraiz\033[m de {}{}{} é {}{}{}.'.format(cores['amarelo.n'], n1, cores['limpo'], cores['azul.n'], r, cores['limpo']))
