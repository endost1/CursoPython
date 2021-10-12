# Exercício Python 099: 
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep # Importando comando sleep #

def maior(* num): # Função maior #
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor} ', end='', flush=True) # Print dos valores #
        sleep(0.5)
        if cont == 0: # Tratamento de resultado #
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'E o maior número foi {maior}')


# Valores #
maior(2, 5, 6, 9, 1) 
maior(5, 5, 3, 2)
maior(9, 10, 1)
maior(11, 3)
maior(1)
maior()
