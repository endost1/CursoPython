# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# data atual:
from datetime import date
at = date.today().year
tma = 0
tme = 0
for pess in range(1, 8):
# idade:
    d = int(input(f'Em que ano a {pess}º pessoa nasceu? '))
    i = at - d
    if i >= 21:
        tma += 1
    else:
        tme += 1
print('-=' * 20)
print(f'Ao todo tivemos {tma} pessoas maior de idade!')
print(f'Ao todo tivemos {tme} pessoas menor de idade!')