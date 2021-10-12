# Exercício Python 100: 
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre 
# todos os valores pares sorteados pela função anterior.

from random import randint # Importando o comando randint #
from time import sleep # Importando o comando sleep #

def sorteia(lista): # Função para sortear #
    print('Sorteando 5 valores... ', end='')
    for cont in range(0, 5):
        n = randint(1, 10) # Sorteando valores entre 1 e 10 #
        lista.append(n)
        print(f'{n} ',end='', flush=True) # Print valores #
        sleep(0.5)
    print('FIM!')
        

def somaPar(lista): # Função para somar os números pares #
    soma = 0
    for valor in lista: 
        if valor % 2 == 0: # Tratamento de valores #
            soma += valor # Somando os valores #
    print(f'A soma dos números pares da lista {lista} é igual a: {soma}') 

# Programa principal #
numero = list()
sorteia(numero)
somaPar(numero)
