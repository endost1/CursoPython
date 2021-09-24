# Exercício Python 094: 
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoas = {} # Criando meu dicionário #
galera = [] # Crianodo uma lista #
soma = media = 0 # Variaveis para cálculos #

while True: # Iniciando um laço para armazenar dados #
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')) # Adicionando o nome #
    pessoas['Idade'] = int(input('Idade: ')) # Adicionando a idade #
    while True: # Laço para selecionar o sexo da pessoa #
        print('''        
        [ 1 ] Masculino
        [ 2 ] Feminino
        ''')
        sexo = int(input('Sexo: '))
        if sexo == 1:
           pessoas['Sexo'] = 'M'
        if sexo == 2:
            pessoas['Sexo'] = 'F'
        if sexo in (1, 2):
            break
        else: # Mensagem de erro #
            print('~' * 30)
            print('ERRO!: Por favor, digite apenas os números informados a tela.')
            print('~' * 30)
    soma += pessoas['Idade'] # Somando as idades #
    galera.append(pessoas.copy()) # Adicionando os dicionários a lista #
    while True: # Iniciando laço para continuar ou não com o programa #
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resposta in 'SN':
            break
        else: # Mensagem de erro #
            print('ERRO!: Por favor, digite apenas S ou N.')
    if resposta in 'Nn': # Condição para sair do laço #
        break
# Imprimindo na tela os resultados #
print('-=' * 15)
print(f'A) Foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'B) A média de idade é igual a {media:.2f} anos')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('D) As pessoas com idade acima da média é: ', end='')
for p in galera:
    if p['Idade'] >= media:
        print('',end='')
        print()
        for k, v in p.items():
            print(f'{k} => {v}', end=' ; ')
    print()
print('-=' * 15)
print('  >>  > THE END <  <<  ')
