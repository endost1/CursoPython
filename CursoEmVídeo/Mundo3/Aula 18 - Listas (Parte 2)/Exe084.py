pessoas = list()
dados = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados)
    dados.clear()
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta in 'Nn':
        break

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
