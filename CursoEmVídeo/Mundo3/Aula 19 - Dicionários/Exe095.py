# Exercício Python 095: 
# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {} # Criando o dicionário
jogadores = [] # Criando a lista para auxiliar na tarefa
partidas = [] # Criando a lista de partidas, armazenar os gols
print(f'{" >> LISTA DE JOGADORES << ":^35}')
print('~' * 40)
while True: # Laço para cadastrar os jogadores #
    print('-')
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')) # Adicionando o nome do jogador
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? ')) # Adicionando a quantidade de partidas jogadas
    partidas.clear()
    for c in range(0, tot): # Criando um laço para armazenar quantos gols foram feito em cada partida
        partidas.append(int(input(f'Quantos gols na {c+1}º partida? '))) # utilizando a lista
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas) # Somando o total de gols feito
    jogadores.append(jogador.copy()) # Adicionando os dicionários a lista #
    while True: # Laço para adicionar mais cadastros #
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERRO!: Por favor, digite apenas S ou N')
    if resposta in 'Nn':
        break
 # Imprimindo resultado #
print('-=' * 20)
print(f'{" >> QUADRO DE JOGADORES << ":^35}')
print('- ' * 20)
print('Cod.  ', end='')
for i in jogador.keys():
    print(f'{i:<12}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:<3} - ', end='')
    for d in v.values():
        print(f'{str(d):<12}', end='')
    print()
print('-=' * 20)

while True: # Laço para o sistema de visualização dos detalhes do aproveitamento de cada jogador #
    print('-=' * 20)
    opcao = int(input('Quer ver os detalhes de qual jogador? [999 interrompe] '))
    if opcao == 999:
        break
    if opcao >= len(jogadores):
        print('ERRO!: Jogador não existente no banco de dados.')
    else:
        print(f' : LEVANTAMENTO do jogador {jogadores[opcao]["Nome"]}')
        for i, v in enumerate(jogadores[opcao]["Gols"]):
            print(f' No {i+1}º jogo fez {v} gols')
    print('-=' * 20)
print('- ' * 20)
print(F'{"  >>>  THE END  <<<  ":^35}')
