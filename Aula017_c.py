valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

print(f'Valores: {valores}')

print('Valores: ', end='')
for v in valores:
    print(f'{v}', end='')
    if v == len(valores) + 1:
        print(end='.')
    else:
        print(end='; ')
print(end='\n')
print('{:>12}'.format('VALORES'))
for c, v in enumerate(valores):
    print(f'{"Key":>7} {c}: {v}')