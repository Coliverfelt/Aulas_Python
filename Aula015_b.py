nome = 'Carol'
idade = 25
salario = 2500.45

print(f'A {nome:^30} tem {idade} anos e ganha R${salario:.2f}.') #PYTHON 3.6+
print('A {:^5} tem {} anos e ganha R${:.2f}.'.format(nome, idade, salario)) #PYTHON 3
print('A %s tem %d anos e ganha R$%.2f.' %(nome, idade, salario)) #PYTHON 2