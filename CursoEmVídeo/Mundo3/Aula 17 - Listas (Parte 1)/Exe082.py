# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

# criando uma lista:
valores = list()
valor_par = list()
valor_impar = list()
# criando um while para armazenar n valores:
while True:
    valores.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta in 'N':
        break
# criando um for para analisar quais números são pares ou impares:
for i, v in enumerate(valores):
    if v % 2 == 0:
        valor_par.append(v)
    else:
        valor_impar.append(v)
# imprimindo resultado:
print(f'Lista completa: {valores}')
print(f'Lista de pares: {valor_par}')
print(f'Lista de impares: {valor_impar}')
