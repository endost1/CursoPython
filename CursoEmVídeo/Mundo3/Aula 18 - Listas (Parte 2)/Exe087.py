# Exercício Python 087: 
# Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # criando minha matriz 3x3
soma_par = soma_coluna = maior =  0 # adicionando novas variaives
for linha in range(0, 3): # criando laço para armazenar dados na matriz criada
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digita um valor para a posição [{linha}, {coluna}]: '))
print('-=' * 25)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]', end='') # imprimindo a matriz na tela com a formatação correta
        if matriz[linha][coluna] % 2 == 0: # condição para somar os números pares da matriz
            soma_par += matriz[linha][coluna]
    print()
print('-=' * 25)
print(f'A soma entre os valores pares digitados é igual a: {soma_par}')
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é igual a: {soma_coluna}')
if coluna == 0:
    maior = matriz[1][coluna]
else:
    maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é: {maior}')
