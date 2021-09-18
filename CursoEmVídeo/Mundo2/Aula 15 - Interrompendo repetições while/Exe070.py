ct = cmil = m = c = 0
b = ''
while True:
    print('{:-^40}'.format(' LISTA DE COMPRAS '))
    print('-' * 40)
    n = str(input('Nome do Produto: '))
    v = float(input('Valor: R$'))
    c += 1
    ct += v
    if v > 1000:
        cmil += 1
    if c == 1 or v < m:
        m = v
        b = n
    querer = ' '
    while querer not in 'SN':
        querer = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if querer == 'N':
        break
print('{:-^40}'.format(' PROGRAMA FINALIZADO '))
print(f'''
O total da compra foi R${ct:.2f}.
Total de produtos com valor acima de R$1000.00: {cmil}
O produto mais barato: {b}
''')