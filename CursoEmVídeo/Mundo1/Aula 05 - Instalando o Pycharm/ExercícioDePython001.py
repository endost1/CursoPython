#add cores
cores = {'limpo':'\033[m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}
print('{}Olá Mundo!{}'.format(cores['verde'], cores['limpo']))
