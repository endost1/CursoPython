# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print(f'{"CONTAGEM REGRESSIVA PARA OS FOGOS":=^20}')
print('-=' * 10)
for contagem_regressiva in range(10, -1, -1):
    print(contagem_regressiva)
    sleep(1)
print('-=' * 10)
print('"ESTOURA OS FOGOS DE ARTIFÍCIOS"!')
print('-=' * 10)
print('FIM DO ALGORITMO!')