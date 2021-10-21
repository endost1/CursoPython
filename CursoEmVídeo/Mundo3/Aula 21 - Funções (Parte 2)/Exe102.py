# Exercício Python 102: 
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se 
# será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False): # Função fatorial #
    """
    -> Calcular o fatorial de um número:
    :param n: O número a ser calculado.
    :param show: (Opcional) mostrar o calculo na tela.
    :return: Retornar o valor.
    """
    f = 1 # Número base inicial #
    for c in range(n, 0, -1): # Principio do fatorial #
        if show: # Condição para mostrar o calculo #
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c # Calculando #
    return f # Retornando resultado final #

# Programa Principal #
print(fatorial(5, show=True))
# help(fatorial) #
