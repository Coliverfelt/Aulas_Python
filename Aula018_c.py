galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])# [:] -> Cópia da estrutura dados
    dado.clear()# Clear em Dodas e Galera, pois eles estão ligados

print(galera)

tMaior = tMenor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        tMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tMenor += 1

print(f'Temos {tMaior} pessoas maiores de idade e {tMenor} menor.')