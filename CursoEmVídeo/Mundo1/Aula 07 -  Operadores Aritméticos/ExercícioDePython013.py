# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m',
         'roxo.n': '\033[1;35m',
         'cinza.n': '\033[1;37m',
         'ciano.n': '\033[1;36m' }

print('{}Áfim de saber qual será seu salário com 15% de aumento?{} '.format(cores['vermelho.n'], cores['limpo']))

s = float(input('{}Digite seu salário atual:{} '.format(cores['roxo.n'], cores['limpo'])))

a = s + (s * 15 / 100)

print('Seu salário era de {}R${:.2f}{}, e com um aumento de \033[1;32m 15% \033[m ficou de {}R${:.2f}{}!'.format(cores['amarelo.n'], s, cores['limpo'], cores['amarelo.n'], a, cores['limpo']))
