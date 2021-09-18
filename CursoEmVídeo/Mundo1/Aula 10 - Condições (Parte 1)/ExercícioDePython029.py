print('----Radar eletrônico----')
v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi multado!')
    print('O valor da multa foi de R${:.2f}'.format((v - 80) * 7.00))
else:
    print('Você se safou, dessa vez!')
