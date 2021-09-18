# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m'}

print('{}Quer converter seu dinheiro de reais para dolar?{}'.format(cores['azul.n'], cores['limpo']))

d = float(input('Digite a quantia: R$'))

c = d / 5.03

print('Convertende seu dinheiro, você tem {}US${:.2f}{}!'.format(cores['vermelho.n'], c, cores['limpo']))
