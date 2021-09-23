# Exercício 091:
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.

from random import randint # Importando o randint para sortear números aleatórios
from time import sleep # Importando o sleep para marcar o tempo de resposta
from operator import itemgetter # Importando o itemgetter para ordenar os valores do dicionário 

dado = {
    'Jogador_1' : randint(1, 6),
    'Jogador_2' : randint(1, 6),
    'Jogador_3' : randint(1, 6),
    'Jogador_4' : randint(1, 6),
    } # Criando o dicionário para armazenar os dados de cada jogador
ranking = [] # Criando lista para ajuda na hora de ordenar o dicionário
print('-=' * 15)
print('  >>>  RESULTADOS  <<<  ')
print('~' * 25)
for k, v in dado.items(): # Imprimindo na tela o resultado das jogadas
    print(f'{k} : {v}')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True) # Ordenando a lista com o dicionário
print('-=' * 15)
print('  >>>   RANKING   <<<  ')
print('~' * 25)
for i, v in enumerate(ranking): # Imprimindo na tela a lista ordenada com os dados do dicionário 
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
print('-=' * 15)
print('  >>  THE END  <<  ')
