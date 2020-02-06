nome = str(input('Qual é seu nome? '))

if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

print('Que nome lindo você tem!'if nome=='Gustavo'else'Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))