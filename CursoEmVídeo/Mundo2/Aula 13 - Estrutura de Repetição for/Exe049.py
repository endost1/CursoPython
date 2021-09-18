# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print(f'{"TABUADA":=^20}')
n = int(input('Digite o numero que deseja: '))
for t in range(1, 11):
    print(f'{n} x {t} = {n*t}')
print('-=' * 20)
print('FIM DO ALGORITIMO!')
