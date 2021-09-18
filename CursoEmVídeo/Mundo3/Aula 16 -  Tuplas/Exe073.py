#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Bahia.
tabela = ('Flamengo','Internacional','Atlético-MG','São Paulo','Fluminense','Grêmio','Palmeiras','Santos','Athletico-PR',
          'Bragantino','Ceará','Corinthians','Atlético-GO','Bahia','Sport','Fortaleza','Vasco','Goiás','Coritiba','Botafogo')
print('-' * 40)
print(f'Os cinco primeiros da tabela são: {tabela[:5]}')
print('-' * 40)
print(f'Os ultimos quatros da tabela: {tabela[:-4]}')
print('-' * 40)
print(f'Bahia se econtra na posição: {tabela.index("Bahia") + 1}ª')
print('-' * 40)
