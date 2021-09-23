# Exercício 090:
# Faça um programa que leia nome e média de um aluno, guardando também a situação do aluno em um dicionário.
# No final, mostre o conteudo da estrutura na tela

from time import sleep # Importando o sleep para marcar o tempo de resposta

ficha = {} # Criando o dicionário
ficha['aluno'] = str(input('Aluno: ')) # Adicionando o nome do aluno no dicionário
ficha['média'] = float(input('Média do aluno: ')) # Adicionando a média do aluno no dicionário
if ficha['média'] >= 7: # Criando uma condição de situação: APROVADO ou REPROVADO
    ficha['situação'] = 'Aprovado'
else:
    ficha['situação'] = 'Reprovado'
print('-=' * 10)
for k, v in ficha.items(): # Imprimindo na tela o resultado
    print(f'{k} : {v}')
    sleep(1)
print('-=' * 10)
print('  >>  THE END  <<  ')
