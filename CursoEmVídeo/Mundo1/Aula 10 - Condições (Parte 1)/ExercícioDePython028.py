from random import choice
print('Adivinhe um número de 0 a 5, que o computador escolheu!')
n = [0, 1, 2, 3, 4, 5]
choice(n)
d = input('Digite o número que você acha que foi escolhido: ')
if choice(n):
    print('Você acertou!')
else:
    print('Você errou!')
