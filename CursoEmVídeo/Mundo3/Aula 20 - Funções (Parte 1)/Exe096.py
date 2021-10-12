# Exercício Python 096: 
# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno.

def escreva(msg): # Função escreva #
    tamanho = len(msg) + 4
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)


def area(largura, comprimento): # Função área #
    A = largura * comprimento
    print('-' * 21)
    print(f'A área de um terreno ({largura:.1f} x {comprimento:.1f}) é igual á {A}')


escreva('TABELA DO TERRENO')
l = float(input('Largura (m): ')) # Entrada do valor da largura #
c = float(input('Comprimenot (m): ')) # Entrada do valor do comprimento #
area(l, c) # Passando resultados para a função área #
