# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
c = randint(0, 10)
print('Sou seu computador'
      'E acabei de pensar em número, entre 0 e 10!')
print('Será que vcoê consegue adivinhar?')
acertou = False
p = 0
while not acertou:
    j = int(input('Seu palpite? '))
    p += 1
    if j == c:
        acertou = True
    else:
        if j < c:
            print('Mais... Tente mais uma vez:')
        else:
            print('Menos... Tente mais uma vez:')
print(f'O jogador conseguiu acertar com {p} tentativas. Parabéns!')
