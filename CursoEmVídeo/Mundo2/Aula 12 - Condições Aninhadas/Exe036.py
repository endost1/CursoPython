from math import trunc
# FINANCIANDO UMA CASA:
casa = float(input('Digite o valor da casa a ser fananciada: R$'))
salario = float(input('Digite seu salaário: R$'))
anos = float(input('Digite por quantos anos quer financiar: '))
# PARCELA MENSAL A PAGAR SEM EXECEDER 30% DO SALARIO:
mensalidade = casa / (anos * 12)
exceder = salario * 0.30
print(f'Para pagar uma casa de {casa:.2f} em {trunc(anos)} anos com um salário de R${salario:.2f}, a prestação será de {mensalidade:.2f}')
# CONDIÇÕES DO ALGORITMO:
if exceder <= mensalidade:
    print('FINANCIAMENTO CONCEDIDO!')
else:
    print('FINANCIAMENTO NEGADO!')
