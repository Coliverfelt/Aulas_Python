frase = 'Curso em Vídeo Python'
frase1 = '   Curso em Vídeo Python   '

print(frase)
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))

print(len(frase))
print(len(frase1))
print(len(frase1.strip()))

print(frase.replace('Python', 'Android'))
print(frase)

frase2 = frase.replace('Python', 'Android')
print(frase2)

print('Curso' in frase)
print('Carol' in frase)

print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.find('Carol'))

print(frase.capitalize())
print(frase.title())

frase3 = ('     Carol     ')
print(frase3)
print('Eu sou', frase3.strip())

print('Eu sou', frase3.ljust(10, "!"))

print(frase.split())
split = frase.split()
print(split[0])
print(split[3])
print(split[2][4]) #Quinto caracter do terceiro range
print(split[0][1]) # [Range][Caracter]
frase4 = ('!.!-Carol-!.!')
print(frase4.strip('!.!-'))