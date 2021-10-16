# Exercício Python 101: 
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano): # Criando a função voto #
    from datetime import date # Escopo de importação #
    atual = date.today().year # PEgando o ano atual #
    idade = atual - ano # Calculando idade #
    # Analisando resultados #
    if 18 <= idade <= 70:
        return f'Com {idade} anos: Voto OBRIGATÓRIO.'
    if 16 <= idade < 18 or ano > 70:
        return f'Com {idade} anos: Voto OPCIONAL.'
    else:
        return f'Com {idade} anos: Voto NEGADO.'   

# Programa principal #
anoNascimento = int(input('Em que ano você nasceu? ')) # Entrada de valor #
print('-' * 30)
print(voto(anoNascimento)) # Escrevendo na tela o resultado #
print('~' * 30)
print('      FIM DO PROGRAMA!')
