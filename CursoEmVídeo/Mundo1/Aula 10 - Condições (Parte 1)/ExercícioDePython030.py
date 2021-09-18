print('----PAR OU IMPAR?----')
n = int(input('Digite um número qualquer: '))
r = n % 2
if r == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é ÍMPAR!'.format(n))
