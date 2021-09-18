#add cores
a = input('Digite algo:')

cores = {'limpo':'\033[m',
        'vermelho.n':'\033[1;31m',
        'verde.n':'\033[1;32m',
        'amarelo.n':'\033[1;33m',
        'azul.n':'\033[1;34m' }

print('O tipo primitivo desse valor é:', cores['amarelo.n'], type(a), cores['limpo'])
print('É um número?', cores['verde.n'], a.isnumeric(), cores['limpo'])
print('É alfabético?', cores['verde.n'], a.isalpha(), cores['limpo'])
print('É alfanúmerico?', cores['verde.n'], a.isalnum(), cores['limpo'])
print('Está em maiúsculo?', cores['verde.n'], a.isupper(), cores['limpo'])
print('Está em minúsculo', cores['verde.n'], a.islower(), cores['limpo'])
print('Está capitalizado?', cores['verde.n'], a.istitle(), cores['limpo'])