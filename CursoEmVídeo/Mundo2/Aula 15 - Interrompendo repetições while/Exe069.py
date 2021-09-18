from time import sleep
t = h = m = 0
while True:
    p = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo:[M/F] ')).strip().upper()[0]
    if p >= 18:
        t += 1
    if s == 'F' and p < 20:
        m += 1
    if s == 'M':
        h += 1
    querer = ' '
    while querer not in 'SN':
        querer = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if querer == 'N':
        break
print('Finalizando...')
sleep(2)
print('-=' * 40)
print('Porgrama finalizado. Volte semrpe!')
print('~' * 20)
sleep(1.5)
print(f'''
Foram cadastradas {t} pessoas com idade acima de 18 anos.
Foram cadastrados {h} homens.
Foram cadastradas {m} mulheres com idade acima de 20 anos.''')