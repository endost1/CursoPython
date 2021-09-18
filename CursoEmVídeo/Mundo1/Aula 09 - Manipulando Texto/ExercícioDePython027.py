no = str(input('Digite seu nome completo: ')).strip()
no1 = no.split()
print('Seu primeiro nome é {}.'.format(no1[0]))
print('Seu ultimo nome é {}.'.format(no1[len(no1)-1]))
