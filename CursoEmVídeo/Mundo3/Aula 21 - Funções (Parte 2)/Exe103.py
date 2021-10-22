# Exercício Python 103: 
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gols=0): # Função ficha do jogador #
    """
    -> Ficha dos jogadores
    :param jogador: (opcional) O nome do jogador
    :param gols: (opcional) A quantidade de gols
    :param return: False
    """
    print(f'O jogador {jogador} fez {gols} gols no campeonato.') # Print da função #

# Programa principal #
j = str(input('Digite o nome do jogador: ')) # Entrada de dados #
g = str(input('Número de gols: ')) # Entrada de dados #
if g.isnumeric(): # Condição para trocar o "g" de str para int #
    g = int(g)
else:
    g = 0
if j.strip() == '': # Condição para imprimir na tela #
    ficha(gols=g)
else:
    ficha(j, g)
    
# help(LeiaInt) #
