# add cores
cores = {'limpo': '\033[m',
         'vermelho.n': '\033[1;31m',
         'verde.n': '\033[1;32m',
         'amarelo.n': '\033[1;33m',
         'azul.n': '\033[1;34m'}

print('Quer saber a tabuado de qual número?')

n = int(input('Digite um número:'))
a = n * 0
b = n * 1
c = n * 2
d = n * 3
e = n * 4
f = n * 5
g = n * 6
h = n * 7
i = n * 8
j = n * 9
k = n * 10

print('{}{}{}x0={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], a, cores['limpo']))
print('{}{}{}x1={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], b, cores['limpo']))
print('{}{}{}x2={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], c, cores['limpo']))
print('{}{}{}x3={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], d, cores['limpo']))
print('{}{}{}x4={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], e, cores['limpo']))
print('{}{}{}x5={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], f, cores['limpo']))
print('{}{}{}x6={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], g, cores['limpo']))
print('{}{}{}x7={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], h, cores['limpo']))
print('{}{}{}x8={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], i, cores['limpo']))
print('{}{}{}x9={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], j, cores['limpo']))
print('{}{}{}x10={}{}{}'.format(cores['vermelho.n'], n, cores['limpo'], cores['verde.n'], k, cores['limpo']))
