n1 = float(input('Digite o primeiro seguimento: '))
n2 = float(input('Digite o segundo seguimento: '))
n3 = float(input('Digite o terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os três segmentos PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os três segmentos NÃO PODEM FORMAR UM TRIÂNGULO!')
