from random import choice
print('Sorteando um aluno para apresentar!')
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
l = [n1, n2, n3, n4]
e = choice (l)
print('E o(a) sortudo(a) que foi escolhido(a) é: {}!'.format(e))

"""import random
print('Sorteando um aluno para apresentar!')
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
l = [n1, n2, n3, n4]
e = random.choice (l)
print('E o(a) sortudo(a) que foi escolhido(a) é: {}!'.format(e))"""
