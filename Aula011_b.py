a = 3
b = 5
nome = 'Carol'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Os valores são \033[4;33m{}\033[m \033[1;31me\033[m \033[4;36m{}\033[m'.format(a, b))
print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;30;46m', nome, '\033[m'))
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))