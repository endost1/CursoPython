# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

#criando a lista
valores = list()
#criando um for para armazenar 5 valores:
for cont in range(0, 5):
    numeros = (int(input('Digita um número: ')))
    #criando uma condição para ordenar os valores
    if cont == 0 or numeros > valores[-1]:
        valores.append(numeros)
        print('Adicionado ao final da lista')
    else:
        posição = 0
        while posição < len(valores):
            if numeros <= valores[posição]:
                valores.insert(posição, numeros)
                print(f'Adicionado na posição {posição} da lista')
                break
            posição += 1
#imprimindo os valor na tela, ordenados
print('-='*30)
print(f'Os valores digitados foram: {valores}')