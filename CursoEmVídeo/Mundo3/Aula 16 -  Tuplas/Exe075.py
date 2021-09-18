#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares
t = (int(input('Digite o 1ª valor: ')),
     int(input('Digite o 2ª valor: ')),
     int(input('Digite o 3ª valor: ')),
     int(input('Digite o 4ª valor: ')))
print('-' * 40)
print(f'Os valores digitado foram: {t}')
if t.count(9) > 1:
     print(f'O nove aparece {t.count(9)} vezes')
if t.count(9) == 1:
     print(f'O nove aparece {t.count(9)} vez')
if t.count(9) == 0:
     print(f'O valor 9 não foi encontrado!')
if 3 in t:
     print(f'O três aparece na {t.index(3) + 1}ª posição')
else:
     print('O valor 3 não foi encontrado!')
print(f'Os valores pares digitados foram:', end=' ')
for c in t:
     if c % 2 == 0:
          print(c, end=' ')
print(f'\n{"-" * 40}')
#print(type(t))