#add cores
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2

cores = {'limpo':'\033[m',
        'vermelho.n':'\033[1;31m',
        'verde.n':'\033[1;32m',
        'amarelo.n':'\033[1;33m',
        'azul.n':'\033[1;34m'}

print(f'A soma entre {cores["verde.n"]}{n1}{cores["limpo"]} e {cores["amarelo.n"]}{n2}{cores["limpo"]} é igual a {cores["vermelho.n"]}{s}{cores["limpo"]}')