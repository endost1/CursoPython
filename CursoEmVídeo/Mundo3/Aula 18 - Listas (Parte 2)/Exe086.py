# Exercício Python 086: 
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # criando minha matriz 3x3
for linha in range(0, 3): # criando laço para armazenar dados na matriz criada
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digita um valor para a posição [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]', end='') # imprimindo a matriz na tela com a formatação correta
    print()
