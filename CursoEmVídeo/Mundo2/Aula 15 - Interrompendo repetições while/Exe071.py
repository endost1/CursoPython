# va = valor, c = cédula, toc = total de cédulas
print('-' * 30)
print('{:-^30}'.format('CAIXA ELETRÔNICO'))
print('-' * 30)
va = int(input('Digite o valor a ser sacado: R$'))
c = 100
toc = 0
while True:
    if va >= c:
        va -= c
        toc += 1
    else:
        if toc > 0:
            print(f'{toc} cédulas de R${c}')
        if c == 100:
            c = 50
        elif c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        toc = 0
        if va == 0:
            break
print('-' * 30)
print('Agradecemos pela preferência do nosso Banco. Volte sempre!')
'''
print('-' * 30)
print('{:-^30}'.format('CAIXA ELETRÔNICO'))
print('-' * 30)
va = int(input('Digite o valor a ser sacado: R$'))
c = va // 100
re = va % 100
if c > 0:
    print(f'{c} cédulas de R$100 reais')
c = re // 50
re %= 50
if c > 0:
    print(f'{c} cédulas de R$50 reais')
c = re // 20
re %= 20
if c > 0:
    print(f'{c} cédulas de R$20 reais')
c = re // 10
re %= 10
if c > 0:
    print(f'{c} cédulas de R$10 reais')
c = re // 1
if c > 0:
    print(f'{c} cédulas de R$1 real')
print('-' * 30)
print('Agradecemos a escolha do nosso Banco. Volte sempre!')
'''