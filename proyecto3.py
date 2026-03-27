texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit python"
texto = texto.lower()
letras = ['a', 'g', 'l']
n=0

# contar letras de la frase
for l in letras:
    print(f'El texto tiene {texto.count(l)} {letras[n]}')
    n+=1

palabras = texto.split()

print(f'El texto tiene {len(palabras)} palabras')

print(f'inicia con {texto[0]}')

invertido = texto[::-1]
print(f'Termina con {invertido[0]}')

print(invertido)

encontro = 'no'
for p in palabras:
    if p == 'python':
        encontro = 'si'
        break
    else:
        pass
print(encontro)
