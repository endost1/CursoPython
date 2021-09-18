d = float(input('Digite a distância da sua viagem: '))
print('Você vai fazer uma viagem de {:.0f}km'.format(d))
if d <= 200:
    print('O valor a ser pago é de R${:.2f}'.format(d * 0.50))
else:
    print('O valor a ser pago é de R${:.2f}!'.format(d * 0.45))
