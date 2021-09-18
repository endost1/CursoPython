n1 = float(input('Digite o primeiro seguimento: '))
n2 = float(input('Digite o segundo seguimento: '))
n3 = float(input('Digite o terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os três segmentos podem formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('ISÓSCELES')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
else:
    print('Os segmentos não podem formar um triângulo')
