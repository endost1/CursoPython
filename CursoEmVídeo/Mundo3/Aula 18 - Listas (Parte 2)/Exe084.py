#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
maior = menor = 0

while True: # Criando um laço infinito para armazenar dados
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0: # Criando uma Codição para o maior e menor peso
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados)
    dados.clear()
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0] # Codição para quebra ou não do laço
    if resposta in 'Nn': # qubrando o laço infinito
        break

# Imprimindo resultado da questão

print()
print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso cadastrado foi {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso cadastrado foi {menor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end='')
