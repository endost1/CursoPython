from time import sleep
n = c = 0
while True:
    print('-' * 80)
    n = int(input('Quer a tabuada de qual número?(Condição de parada: número negativo): '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
print('~' * 80)
print('ENCERRANDDO PROGRAMA...')
sleep(1.5)
print('Programa encerrado. Volte sempre!')