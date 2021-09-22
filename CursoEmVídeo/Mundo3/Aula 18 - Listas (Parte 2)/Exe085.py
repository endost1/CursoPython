# Exercício Python 085: 
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única.
# Separando os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
from time import sleep

numeros = [[], []] # criar a lista
valor = 0
for c in range(0, 7): # criar laço para armazenar 7 valores
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0: # validar dados, se é par ou impar
        numeros[0].append(valor)
    elif valor % 2 == 1:
        numeros[1].append(valor)
print('~' * 50)
print('   << Organizando Resultado >>   ')
sleep(1.5)
print('-=' * 25) # imprimir o resultado na tela
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números impares digitados foram: {numeros[1]}')
print('-=' * 25)
print('     <<<   Finalizado   >>>   ')
print('~' * 50)
