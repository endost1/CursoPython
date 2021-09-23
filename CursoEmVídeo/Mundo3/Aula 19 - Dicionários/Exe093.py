# Exercício 093:
# Crie um programa que leia o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feita em cada partida.
# No final, tudo isso irar ser guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {} # Criando o dicionário
gols = [] # Criando a lista para auxiliar na tarefa
print(f'{" >> APROVEITAMENTO DO JOGADOR << ":^35}')
print('~' * 40)
jogador['Nome'] = str(input('Nome do jogador: ')) # Adicionando o nome do jogador
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? ')) # Adicionando a quantidade de partidas jogadas
for c in range(0, jogador['Partidas']): # Criando um laço para armazenar quantos gols foram feito em cada partida
    gols.append(int(input(f'Quantos gols na {c+1}º partida? '))) # utilizando a lista
jogador['Gols'] = gols[:] # Adicionando a lista no dicionário
jogador['Total de Gols'] = sum(gols) # Somando o total de gols feito
print('-=' * 20)
print(f'O {jogador["Nome"]} jogou {jogador["Partidas"]} partidas!') # Imprimindo na tela o nome e a quantidade de partidas jogadas
print('-=' * 20)
for i, v in enumerate(jogador['Gols']): # Imprimindo na tela as partidas e quantos gols foram feitos em cada um
    print(f' >>> Na {i+1}º partida fez {v} gols')
print('-=' * 20)
print(f' >>> TOTAL DE GOLS: {jogador["Total de Gols"]}') # Imprimindo na tela o total de gols feito
print('~' * 40)
print(f'{"  >>  THE END  <<  ":^35}')
