# Exercício Python 089: 
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

alunos = []
while True:
    nome = str(input('Nome do Aluno: '))
    nota1 = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda Nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta in 'Nn':
        break
print('-' * 20)
print(f'{"Nº":<4}{"Nome":<6}{"Média":>8}')
print('-' * 20)
for indice, aluno in enumerate(alunos):
    print(f'{indice:<4}{aluno[0]:<6}{aluno[2]:>8.1f}')
while True:
    print('-' * 20)
    opcao = int(input('Quer ver a nota de qual aluno [999 encerra]: '))
    if opcao == 999:
        print('~' * 20)
        print('FINALIZANDO...')
        sleep(1.5) 
        break
    if opcao <= len(alunos) -1:
        print(f'{alunos[opcao][0]}: {alunos[opcao][1]}')
