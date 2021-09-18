# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
s = c = media = maior = menor = 0
re = 'S'
while re in 'S':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    re = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
media = s / c
print(f'Você digitou {c} números e a média entre eles foi de {media}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')