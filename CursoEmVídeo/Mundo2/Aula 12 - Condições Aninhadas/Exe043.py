peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
altura_ao_quadrado = altura ** 2
imc = peso / altura_ao_quadrado
print(f'Você tem um imc de {imc:.2f}, e está ',end='')
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('com o PESO IDEAL')
elif 25 <= imc < 30:
    print('com SOBREPESO')
elif 30 <= imc < 40:
    print('com OBESIDADE')
else:
    print('com OBESIDADE MORBIDA')
