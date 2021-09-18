# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''idade = int(input('Digite sua idade: '))
if idade == 18:
    print('Essa é a hora exata para você se alistar no exército!')
elif idade < 18:
    print(f'Ainda não está na hora de se alistar, lhe falta {18 - idade} anos para poder entrar no exército, continue com essa vontade!')
else:
    print(f'Você já passou do tempo de se alistar faz {idade - 18} anos.')'''

from _datetime import date

atual = date.today().year

sexo = str(input('Digite seu sexo: '))

ano = int(input('Ano de nascimento: '))

idade = atual - ano

if sexo == 'masculino':
    if idade == 18:
        print(f'Você nasceu em {ano} e sua idade é {idade} anos, e no ano atual de {atual}, está na HORA EXATA de se alistar!')
    elif idade < 18:
        print(f'Você nasceu em {ano} e sua idade é {idade} anos, e no ano atual de {atual}, não está na hora ainda para se alistar, ainda lhe falta {18 - idade} anos. Irar poder se alistar em {ano + (18 - idade)}!')
    else:
        print(f'Você nasceu em {ano} e sua idade é {idade} anos, e no ano atual {atual}, você já passou da hora de se alistar, faz {idade - 18} anos!. Você deveria ter feito o alistamento em {2021 - (idade - 18)}')
else:
    print('Você não precisa fazer o alistamento!')
