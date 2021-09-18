# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

valor_a_pagar = int(input('Digite o valor da compra: R$'))
print('[ 1 ] no dinheiro a vista?. 10% de desconto')
print('[ 2 ] no cartão a vista?. 5% de desconto')
print('[ 3 ] em até 2x no cartão?. valor formal')
print('[ 4 ] 3x ou mais no cartão?. 20% de juros')
forma_de_pagamento = int(input('Digite um dos respectivos números acima, que se refira a forma de pagamento que prefere: '))
if forma_de_pagamento == 1:
    print(f'O valor a pagar é de R${valor_a_pagar - (valor_a_pagar * 0.1):.2f}. SEM JUROS')
elif forma_de_pagamento == 2:
    print(f'O valor a pagar é de R${valor_a_pagar - (valor_a_pagar * 0.05):.2f}. SEM JUROS')
elif forma_de_pagamento == 3:
    print(f'O valor a pagar é o mesmo da compra R${valor_a_pagar}. SEM JUROS')
else:
    total = valor_a_pagar + (valor_a_pagar * 0.2)
    total_de_parcela = int(input('Quantas parcelas? '))
    parcela = total / total_de_parcela
    print(f'Sua compra será parcela em {total_de_parcela}x, com parcelas de R${parcela:.2f}. COM JUROS')
    print(f'O valor de R${valor_a_pagar:.2f} passou a custar R${total:.2f}.')
