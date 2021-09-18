print('A sua cidade começa coma palavra santo?')
no1 = str(input('Digite o nome da sua cidade: ')).strip()
print(no1[:5].lower() == 'santo')
