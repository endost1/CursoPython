# Exercício Python 104: 
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def LeiaInt(msg): # Função LeiaInt #
    ok = False # Condição inicial #
    valor = 0 # Condição inicial #
    while True: # Laço infinito para trabalhar os dados #
        n = str(input(msg)) # passando como vai ser a função #
        if n.isnumeric(): # Condição para função LeiaInt #
            valor = int(n)
            ok = True
        else: # Tratamento de erro #
            print('\033[0;031mERRO! Você digitou um valor inválido!\033[m')
        if ok:
            break
    return valor # Retornando o valor #

# Programa Principal #
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')
