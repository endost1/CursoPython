# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
contagem = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
            'doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
al = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 > al or al > 20:
        al = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você escolheu o número {contagem[al]}')
