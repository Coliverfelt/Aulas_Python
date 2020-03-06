import math
#from math import sqrt

n = int(input('Digite um número: '))
raiz = math.sqrt(n)

print('A raiz quadrada de {} é {}.'.format(n, raiz))
print('----------Arredondando----------')
print('A raiz quadrada de {} é {:.2f}.'.format(n, raiz))
print('----------Arredondando para cima----------')
print('A raiz quadrada de {} é {}.'.format(n, math.ceil(raiz)))
print('----------Arredondando para baixo----------')
print('A raiz quadrada de {} é {}.'.format(n, math.floor(raiz)))
print('----------Truncando----------')
print('A raiz quadrada de {} é {}.'.format(n, math.trunc(raiz)))