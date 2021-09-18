#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('camundongo', 'catedral', 'aranha', 'universidade', 'emilia', 'destruicao')
print('=' * 30)
print(f'{" VOGAIS ":=^30}')
print('=' * 30)
for i in palavras:
        print(f'\n{i:<18}:', end='')
        for letra in i:
                if letra in 'aeiou':
                        print(letra, end=' ')
print(f'\n{"=" * 30}')