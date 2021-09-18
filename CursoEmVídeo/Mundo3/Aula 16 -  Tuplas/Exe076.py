#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
# lis = TUPLA de lista escolar
lis = ("Lápis", 1.75,
       "Borracha", 2.00,
       "Caderno", 15.90,
       "Estojo", 25.00,
       "Transferidor", 4.20,
        "Compasso", 9.99,
       "Mochila", 120.32,
       "Canetas", 22.30,
       "Livro", 34.90)
print('-' * 30)
print(f'{"LISTA DE COMPRAS":-^30}')
print('-' * 30)

for c in range(0, len(lis), 2):
       print(f'{lis[c]:.<20}R${c + 1:>7.2f}|')

'''for c in range(0, len(lis)):
    if c % 2 == 0:
        print(f'{lis[c]:.<20}R$', end='')
    else:
        print(f'{lis[c]:>8.2f}')'''

print('-' * 30)
