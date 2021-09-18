# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma = nota1 + nota2
media = soma / 2
if media >= 7:
    print(f'Média do aluno {media:.1f}, APROVADO!')
elif 7 > media >= 5:
    print(f'Média do aluno {media:.1f}, RECUPERAÇÃO!')
else:
    print(f'Média do aluno {media:.1f}, REPROVADO!')

'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

def calcular_media(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    print(f'Aluno tirou, {media:.1f}')
    return

def verificar_aprovacao(media):
    if media >= 7:
        print('Aluno APROVADO!')
    elif 7 > media >= 5:
        print('Aluno em RECUPERAÇÃO!')
    else:
        print('Aluno REPROVADO!')

aluno = [nota1, nota2]
media = calcular_media(aluno)
verificar_aprovacao(media)
'''