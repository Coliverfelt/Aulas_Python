valores = []
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print('\033[7m{:^15}\033[m'.format("VALORES"))
for c, v in enumerate(valores):
    print(f'{"Key":>7} {c}: {v}')