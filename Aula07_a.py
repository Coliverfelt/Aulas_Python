n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaointeira = n1//n2
exponenciacao = n1**n2
resto = n1 % n2

print('A soma entre os valores {} e {} vale {}'.format(n1, n2, soma), end='. ')
print('A subtração entre os valores {} e {} vale {}'.format(n1, n2, subtracao))
print('A multiplacação entre os valores {} e {} vale {}'.format(n1, n2, multiplicacao))
print('A divisão entre os valores {} e {} vale {:.3f}'.format(n1, n2, divisao))
print('A divisão inteira entre os valores {} e {} vale {}'.format(n1, n2, divisaointeira))
print('A exponeciação entre os valores {} e {} vale {}'.format(n1, n2, exponenciacao))
print('O resto da divisão entre os valores {} e {} vale {}'.format(n1, n2, resto))