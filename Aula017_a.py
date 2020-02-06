lista = [1, 2, 3, 'oi']
print(lista)
lista.append(5) # Insere o valor 4 ao final
print(f'Append (Adiciona ao final da lista) 5: {lista}')
lista.insert(1, 9) # Insere na Key 1, o valor 9
print(f'Insert na Key 1 o valor 9: {lista}')
del lista[0] # Deleta o conteúdo da Key 0
print(f'Deleta o conteúdo da Key 0: {lista}')
lista.pop(4) # Deleta o conteúdo da Key 4
             # Geralmente usado para deletar o conteúdo do final da lista: lista.pop()
print(f'Deleta o conteúdo da Key 4: {lista}')
lista.remove('oi') # Deleta o conteúdo "oi"
print(f'Deleta o conteúdo "oi": {lista}')

print(f'Lista: {lista}')
lista.sort()
print(f'Lista em ordem CRESCENTE: {lista}')
lista.sort(reverse=True)
print(f'Lista em ordem DECRESCENTE: {lista}')