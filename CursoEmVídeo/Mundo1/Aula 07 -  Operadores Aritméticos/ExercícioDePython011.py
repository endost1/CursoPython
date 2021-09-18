# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m',
         'roxo.n': '\033[1;35m',
         'cinza.n': '\033[1;37m',
         'ciano.n': '\033[1;36m' }

print('{}Áfim de saber quantos litros de tinta irar usar, de acordo com a área da parede?{}'.format(cores['vermelho.n'], cores['limpo']))

c = float(input('{}Digite a altura da parede:{} '.format(cores['roxo.n'], cores['limpo'])))

b = float(input('{}Diigite a largura da parede:{} '.format(cores['azul.n'], cores['limpo'])))

a = b * c

l = a / 2

print('A área a ser preechida é de {}{}m²{}, e a quantidade de litros de tinta é de {}{}litros{}!'.format(cores['ciano.n'], a.__trunc__(), cores['limpo'], cores['amarelo.n'], l.__trunc__(), cores['limpo']))
