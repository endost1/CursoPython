from datetime import date
print('----BISSEXTO ou NÃO?----')
a = int(input('Que ano você quer saber? Coloque 0 para saber se o ano atual é: '))
#Pegando a data atual
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(a))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(a))
