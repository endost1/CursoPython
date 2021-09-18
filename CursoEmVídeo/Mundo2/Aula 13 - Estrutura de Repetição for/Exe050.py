s = 0
c = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}º valor: '))
    if n % 2 == 0:
        s += num
        c += 1
print(f'Você informou {c} números pares, e a soma deu {s}')
