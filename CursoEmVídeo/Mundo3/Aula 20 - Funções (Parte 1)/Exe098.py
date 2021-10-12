# Exercício Python 098: 
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
# a) de 1 até 10, de 1 em 1                                                                                                                                              
# b) de 10 até 0, de 2 em 2                                                                                                                                            
# c) uma contagem personalizada

from time import sleep # Importando comando sleep #

def contador(inicio, fim, passo): # Função contador #
    if passo < 0:
        passo *= -1 # Tratamento de erro #
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo}:') # Mensagem #
    sleep(2.5)
    if inicio < fim: # Tratamento de erro #
        cont = inicio
        while cont <= fim: # Contagem #
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:  # Tratamento de erro #
        cont = inicio
        while cont >= fim: # Contagem #
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('  CONTAGEM PERSONALIZADA ')
ini = int(input('Inicio: '))
f = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, f, pas) # Passando dados personalizados para a Função contador #