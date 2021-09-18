f = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(f.lower().count('a')))
print('A primeira letra A apareceu na posição {}.'.format(f.find('a')+1))
print('A ultima letra A apareceu na posição {}.'.format(f.rfind('a')+1))
