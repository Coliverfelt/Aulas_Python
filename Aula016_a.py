# TUPLAS são IMUTÁVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'

print(lanche[3])
print(lanche[-4])
print(lanche[0:2])
print(lanche[-3:-1])
print(lanche[1:])
print(lanche)

print(f'Tenho {len(lanche)} comidas pra comer.')
print('=' * 40)
for i in range(0, len(lanche)):
    print('Eu vou comer {} da posição {}.'.format(lanche[i], i))
print('=' * 40)
print('=' * 40)
for comida in lanche:
    print('Eu vou comer {}.'.format(comida))
print('=' * 40)
print('=' * 40)
for posicao, comida in enumerate(lanche):
    print('Eu vou comer {} da posição {}.'.format(comida, posicao))
print('=' * 40)
print('Comi pra caramba!\n')

print(f'O lanche em ordem é: {sorted(lanche)}')
print(f'Lanche: {lanche}')