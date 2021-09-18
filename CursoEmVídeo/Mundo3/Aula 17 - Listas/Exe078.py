'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = list()
maior = 0
menor = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {cont}:')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('-='*25)
print(f'Os números digitados foram: {valores}')
print(f'O maior número digitado foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}... ', end='')
print()
print(f'O menor número digitado foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}... ', end='')
print()
