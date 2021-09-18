v = float(input('Digite o seu salário: '))
if v <= 1250:
    print('O seu salário de R${:.2f}, agora é de R${:.2f}'.format(v, v + (v * 0.15)))
else:
    print('O seu salário de R${:.2f}, agora é de R${:.2f}'.format(v, v + (v*0.1)))
