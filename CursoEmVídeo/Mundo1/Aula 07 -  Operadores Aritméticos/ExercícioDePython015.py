# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m',
         'roxo.n': '\033[1;35m',
         'cinza.n': '\033[1;37m',
         'ciano.n': '\033[1;36m' }

print('{}Aluguel a pagar do carro!{}'.format(cores['vermelho.n'], cores['limpo']))
d = int(input('{}Por quantos dias você andou?{} '.format(cores['cinza.n'], cores['limpo'])))
a1 = d * 60
k = float(input('{}Quantos quilometros você rodou?{} '.format(cores['cinza.n'], cores['limpo'])))
a2 = k * 0.15
at = a1 + a2
print('O aluguel do carro ficou por {}R${:.2f}{}'.format(cores['ciano.n'], at, cores['limpo']))
