# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        c += 1
        s += n
print(f'''O somatório de todos os {c} números multiplos de 3, no intervalo de 1 até 500, é: 
{s}''')
