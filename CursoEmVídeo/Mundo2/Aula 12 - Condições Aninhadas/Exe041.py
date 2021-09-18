# A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

from _datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
print(f'Idade: {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
