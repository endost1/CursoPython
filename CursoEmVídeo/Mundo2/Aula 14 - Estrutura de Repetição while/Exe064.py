# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = s = c = 0
n = int(input('Digite um número [CONDIÇÃO DE PARADA: 999]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [CONDIÇÃO DE PARADA: 999]: '))
print('Acabou')
print('>'*20)
print(f'Você digitou {c} números e a soma entre eles deu {s}.')
