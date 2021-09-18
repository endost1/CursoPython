# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
# e fechados na ordem correta.

# criando um input para ler uma expressão:
expressao = str(input('Digite uma expressão: '))
# criando uma lista:
parentese = list()
# criando um for para a lógica do algoritmo:
for simbolo in expressao:
    if simbolo == '(':
        parentese.append('(')
    elif simbolo == ')':
        if len(parentese) > 0:
            parentese.pop()
        else:
            parentese.append(')')
            break
# imprimindo na tela os resultados de acordo com a lógica
print('-='*30)
if len(parentese) == 0:
    print('A exoressão digitada é válida! ')
else:
    print('A expressão digitada não é válida! ')
