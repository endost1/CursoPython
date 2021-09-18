# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m'}

print('{}Vamos descobrir sua média?{}'.format(cores['vermelho.n'], cores['limpo']))

n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))

media = 6
m = (n1 + n2) / 2

if media <= m:
    print('Sua média foi {}{}{}'.format(cores['azul.n'], m, cores['limpo']))
else:
    print('Sua média foi {}{}{}'.format(cores['amarelo.n'], m, cores['limpo']))
