# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m',
         'roxo.n': '\033[1;35m',
         'cinza.n': '\033[1;37m',
         'ciano.n': '\033[1;36m' }

print('{}Vamos saber o valor de um produto com 5% de desconto?{}'.format(cores['vermelho.n'], cores['limpo']))

v = float(input('{}Digite o valor do produto:{} '.format(cores['roxo.n'], cores['limpo'])))

d = v - (v * 5 / 100)

print('O valor do produto que era de {}R${:.2f}{}, passou a ser {}R${:.2f}{} com desconto de \033[1;32m 5% \033[m nele!'.format(cores['amarelo.n'], v, cores['limpo'], cores['amarelo.n'], d, cores['limpo']))
