# Exercício Python 088: 
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
# Cadastrando tudo em uma lista composta.

from random import randint # importando bibliotecas para sortear
from time import sleep # importando biblioteca de temporizador

valores = [] # criando primeira lista
jogos = [] # criando segunda lista
print('-=' * 15)
print('     >>>   MEGA SENA   <<<    ')
print('-=' * 15)
quantidade = int(input('Quantos jogos você quer sortear? ')) # entrada de dados
total = 1
while total <= quantidade: # criando laço para armazenar os dados
    contador = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in jogos:
            valores.append(numeros)
            contador += 1
        if contador >= 6:
            break
    valores.sort() # ordenando a lista
    jogos.append(valores[:]) # clonando a primeira lista e adicionando na segunda lista
    valores.clear() # apegando a primeira lista
    total += 1
print('-=' * 15)
print(f'   >>>  SORTEANDO {quantidade} JOGOS  <<<   ')
for indice, linha in enumerate(jogos): # criando um laço para mostrar resultado de forma formatada
    print(f'Jogo {indice+1}: {linha}')
    sleep(1)
print('    >>>   BOA SORTE   <<<    ')
