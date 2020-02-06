a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print(a)
print(b)
print(c)
print(f'O tamanho da tupla C é {len(c)}.')
print(f'O número 5 aparece {c.count(5)} vezes em c.')
print(d)
print(f'O 8 está na posição {d.index(8)}.')
print(f'O 5 está na posição {d.index(5)}.')
print(f'O 5 está na posição {d.index(5, 1)}.')