# n = número, c = contador, s = soma
n = c = s = 0
while True:
    n = int(input('Digite um valor(Condição de parada: 999): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores é igual a {s}!')