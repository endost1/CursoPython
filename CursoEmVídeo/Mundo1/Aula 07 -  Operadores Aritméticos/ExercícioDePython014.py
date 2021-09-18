# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m',
         'roxo.n': '\033[1;35m',
         'cinza.n': '\033[1;37m',
         'ciano.n': '\033[1;36m' }

print('{}Convertor de temperatura em C° para F° e para K°!{}'.format(cores['vermelho.n'], cores['limpo']))

c = int(input('{}Digite a temperatura em C°:{} '.format(cores['roxo.n'], cores['limpo'])))

f = (9 * c / 5) + 32

k = c + 273

print('A temperatura {}{}C°{}, equivale a {}{}F°{} e a {}{}K°{}!'.format(cores['verde.n'], c, cores['limpo'], cores['amarelo.n'], f.__trunc__(), cores['limpo'], cores['amarelo.n'], k.__trunc__(), cores['limpo']))
