from math import sqrt, floor

n = int(input('Digite um número: '))
raiz = sqrt(n)

print('A raiz quadrada de {} é {}.'.format(n, raiz))
print('A raiz quadrada de {} é {:.2f}.'.format(n, raiz))
print('A raiz quadrada de {} é {}.'.format(n, floor(raiz)))