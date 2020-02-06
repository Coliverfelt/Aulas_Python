n = 0

for i in range(0, 6):
    print(i)
print('FIM.')

print('\n')
print('*' * 20)
print('{:1^10}'.format(n))
print('\n')

for i in range(6, 0, -1):
    print(i)
print('FIM.')

print('\n')
print('*' * 20)
print('{:1^10}'.format(n))
print('\n')

for i in range(0, 7, 2):
    print(i)
print('FIM.')

print('\n')
print('*' * 20)
print('{:1^10}'.format(n))
print('\n')

for i in range(0, 100, 5):
    print(i)
print('{:_^20}'.format('FIM'))  