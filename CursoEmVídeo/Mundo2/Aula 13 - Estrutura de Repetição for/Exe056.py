# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_de_idade = 0
media_de_idade = 0
maior_idade_de_homem = 0
mais_velho = ''
total_de_mulheres = 0
for p in range(1, 5):
    print(f'===== {p}º pessoa =====')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    soma_de_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_de_homem = idade
        mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_de_homem:
        maior_idade_de_homem = idade
        mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_de_mulheres += 1
media_de_idade = soma_de_idade / 4
print(f'A média de idade do grupo é de {media_de_idade} anos.')
print(f'O homem mais velho tem {maior_idade_de_homem} anos e se chama {mais_velho}.')
print(f'O total de mulheres com menos de 20 anos é {total_de_mulheres}.')
