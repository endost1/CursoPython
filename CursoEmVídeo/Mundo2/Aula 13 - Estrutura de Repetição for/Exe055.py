# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pess in range(1, 6):
    p = float(input(f'Peso da {pess}º pessoa: '))
    if pess == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')
