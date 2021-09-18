# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
f = str(input('Digite uma frase: ')).strip().upper() #frase
p = f.split() #palavras
j = ''.join(p) #junto
i = j[::-1] #inverso
'''i = '' #inverso
for l in range(len(j) - 1, -1, -1):
    i += j[l]'''
print(f'O inverso de {j} é {i}.')
if i == j:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('NÃO É UM PALÍNDROMO!')