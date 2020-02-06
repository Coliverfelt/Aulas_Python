nome = str(input('Qual é o seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Joyce Creuza Mariana Diana Juliana':
    print('Belo nome feminino.')
else: #Opcional
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))