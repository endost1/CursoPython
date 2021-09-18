#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
t = tuple(random.sample(range(10), 5))
print(f'Os valores sorteados foram: {t}')
print(f'O maior número foi {max(t)}')
print(f'O menor número foi {min(t)}')
print(type(t))
