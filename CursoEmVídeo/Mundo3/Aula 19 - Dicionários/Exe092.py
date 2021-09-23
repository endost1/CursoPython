# Exercício 092:
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contração e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime # Importando o datetime para pegar o ano atual

dados = {} # Criando meu dicionário 
while True: # Criando um laço
    dados['Nome'] = str(input('Nome: ')) # Adicionando o nome ao dicionário
    Ano_de_Nascimento = int(input('Ano de nascimento: ')) # Armazenando o ano de nascimento
    dados['Idade'] = datetime.now().year - Ano_de_Nascimento # Adicionando a idade com auxilio do datetime com o ano de nascimento
    dados['CTPS'] = int(input('Número da carteira de trabalho [0 não tem]: ')) # Adicionando a CTPS
    if dados['CTPS'] == 0: # Condição para quebrar o laço
        break
    else: # Condição para continuar a preencher os dados
        dados['Ano de Contratação'] = int(input('Ano de contratação: ')) # Adicionando o ano de contratação
        dados['Salário'] = float(input('Salário: R$ ')) # Adicionando o salário
        dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de Contratação'] + 35) - datetime.now().year) # Adicionando com quantos anos irar se aposentar
    break
print('-=' * 20)
print(f'{">>  DADOS DA PESSOA <<":^33}')
print('~' * 40)
for k, v in dados.items(): # Imprimindo o resultado
    print(f'{k:<25}|{v:^8}')
print('-=' * 20)
