from random import shuffle
print('Ordem de apresentação do trabalho em grupo!')
n1 = str(input('Digite o nome do primeiro grupo: '))
n2 = str(input('Digite o nome do segundo grupo: '))
n3 = str(input('Digite o nome do terceiro grupo: '))
n4 = str(input('Digite o nome do quarto grupo: '))
l = [n1, n2, n3, n4]
shuffle(l)
print('A ordem das apresentação sera: {}'.format(l))

"""import random
print('Ordem de apresentação do trabalho em grupo!')
n1 = str(input('Digite o nome do primeiro grupo: '))
n2 = str(input('Digite o nome do segundo grupo: '))
n3 = str(input('Digite o nome do terceiro grupo: '))
n4 = str(input('Digite o nome do quarto grupo: '))
l = [n1, n2, n3, n4]
shuffle(l)
print('A ordem das apresentação sera: '.format(l))"""