# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

from time import sleep
#criando lista
valores = list()
#criando o while para armazenar os valores na lista
while True:
    numeros = (int(input('Digite um número: ')))
    if numeros not in valores:
        valores.append(numeros)
        print('Processando...')
        sleep(1)
        print('Valor adicionado com sucesso')
    #removendo números repetidos
    else:
        print('Processando...')
        sleep(1)
        print('O valor já existe, não será adicionado')
    #condicionando caso o úsariao deseje continuar
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0] 
    if resposta in 'N':
        break 
#exibindo os valores em ordem crescente
print('Processando resultado...')
sleep(1)
print('-='*30)
valores.sort()
print(f'Os valores digitados foram: {valores}')
