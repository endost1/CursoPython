# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
if num1 > num2:
    print('O PRIMEIRO número é maior!')
elif num1 == num2:
    print('O DOIS número são iguais, portantanto não há maior nem menor!')
else:
    print('O SEGUNDO número é maior!')
