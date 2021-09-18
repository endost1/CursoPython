# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo:
print('>'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('>'*20)
n = int(input('Quantos termos você quer mostrar? '))
print('>'*20)
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
c = 3
while c <= n:
    pro = t1 + t2
    print(f' → {pro}')
    t1 = t2
    t2 = pro
    c += 1
print(' → Fim')
