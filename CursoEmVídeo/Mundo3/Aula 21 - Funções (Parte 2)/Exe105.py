# Exercício Python 105: 
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário 
# com as seguintes informações:
# – Quantidade de notas                                                                                                                                                  
# – A maior nota                                                                                                                                                                
# – A menor nota                                                                                                                                                              
# – A média da turma                                                                                                                                                      
# – A situação (opcional)

def notas(* n, sit=False):
    """
    -> Função para analisar as notas e a situação da turma
    :param n: Número das notas dos alunos
    :param sit: Situação da turma
    :param return: Retorna o dicionário
    """
    r = {}
    r ['Quantidade'] = len(n)
    r ['Maior'] = max(n)
    r ['Menor'] = min(n)
    r ['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r ['Situação'] = 'Boa'
        if r['Média'] >= 5:
            r ['Situação'] = 'Razoável'
        else:
            r ['Situação'] = 'Ruim'
    return r

resposta = notas(5.0, 7.8, 3.5, 8.0, sit=True)
print(resposta)

# help(notas) #
