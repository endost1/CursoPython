# Escreva um programa em Python que leia um número inteiro qualquer. end=''
# e peça para o usuário escolher qual será a base de conversão:. end=''
# 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases numéricas:
      [ 1 ] para converter em binário
      [ 2 ] para converter em octadecimal
      [ 3 ] para converter em hexadecimal''')
opcao = int(input('Sua opção: '))
# CONDIÇÕES DO ALGORITMO:
if opcao == 1:
    print(f'o número {numero} convertido para Binário é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'o número {numero} convertido para Octadecimal é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'o número {numero} convertido para Hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('Não existe essa opção!. Tente novamente')
