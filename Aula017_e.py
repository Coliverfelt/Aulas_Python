a = [2, 3, 4, 7]
b = a

print(f'\nLista A: {a}')
print(f'Lista B: {b}')

b[2] = 8

print(f'\nLista A: {a}')
print(f'Lista B: {b}')

c = a[:]

print(f'\nLista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')

c[2] = 5

print(f'\nLista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')