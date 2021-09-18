# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m'}

n = int(input('Digite um medida em metros: '))
k = n / 1000
h = n / 100
da = n / 10
d = n * 10
c = n * 100
m = n * 1000

print('A medida de {}{}{} metros corresponde a:'.format(cores['amarelo.n'], n, cores['limpo']))
print('{}{}km{}'.format(cores['amarelo.n'], k, cores['limpo']))
print('{}{}hm{}'.format(cores['amarelo.n'], h, cores['limpo']))
print('{}{}dam{}'.format(cores['amarelo.n'], da, cores['limpo']))
print('{}{}dm{}'.format(cores['amarelo.n'], d, cores['limpo']))
print('{}{}cm{}'.format(cores['amarelo.n'], c, cores['limpo']))
print('{}{}mm{}'.format(cores['amarelo.n'], m, cores['limpo']))
