# Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                
# A) Quantos números foram digitados.                                                                   
# B) A lista de valores, ordenada de forma decrescente.                                             
# C) Se o valor 5 foi digitado e está ou não na lista

from time import sleep
# criando uma lista:
valores = list()
# criando um while para armazenar n valores:
while True:
    valores.append(int(input('Digite um número: ')))
    # criando condição de resposta:
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta in 'N':
        break
print('-='*30)
print('Processando resultado...')
sleep(2)
print(f'A lista digitada tem {len(valores)} valores.')
# transformando a lista em ordem descrescente:d
valores.sort(reverse=True)
print(f'A lista em ordem decrescente é: {valores}')
# analisando lista:
if 5 in valores:
    print('O número 5 foi digitado, e está na lista!')
else:
    print('O valor 5 não foi digitado, e não está na lista!')
