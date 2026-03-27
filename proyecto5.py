from random import choice
import os

lista_palabras = ['hola', 'salamandra', 'taquicardia', 'quesadilla']
eleccion = choice(lista_palabras)
lista_eleccion = list(eleccion)
adivinadas = []
letras_incorrectas = []
for i in lista_eleccion: 
    adivinadas.append('_')
vidas = 6
gano = False

# Línea corregida:
letras_limpias = " ".join(adivinadas)
incorrectas_limpias = ", ".join(letras_incorrectas)

def ganador(adivinadas):
    for i in adivinadas:
        if i == '_':
            return False
    return True

def revisar_letra(intento:str, eleccion:str, adivinadas:list):
    n = eleccion.count(intento)
    indice = 0
    for i in range(0, n):
        # indice = eleccion.index(intento)
        # indice para modificar los guiones de la lista de adivinadas
        indice = eleccion.find(intento) if i == 0  else (eleccion.find(intento, indice + 1))
        print(indice)
        adivinadas[indice] = intento
    return adivinadas

while vidas > 0:
    os.system('cls')
    print(f'\t\t\tJuego de ahorcado\n\n\tvidas: {vidas}\tLetras encontradas: {letras_limpias}')
    print(f'\tLetras incorrectas: {incorrectas_limpias}')

    # Validar que sea correcto lo que se ingresa en el imput
    intento_correcto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    intento = '1'
    while intento not in intento_correcto or len(intento) > 1 or intento in letras_incorrectas:
        intento = input('\tIngresa una letra: ').lower()
        # intento.lower()
        if len(intento) > 1:
            print('\n\tSolo una letra!')
        elif intento in letras_incorrectas:
            print('\n\tEsa letra ya la probaste!')
        elif intento not in intento_correcto:
            print('\n\tCaracter invalida')

    if eleccion.find(intento) == -1: # .find regresa -1 si no se encuentra el caracter en la cadena
        vidas -= 1
        letras_incorrectas.append(intento)
        incorrectas_limpias = ", ".join(letras_incorrectas)
        print('\tLetra no encontrada')
        os.system('pause')
    else:
        adivinadas = revisar_letra(intento, eleccion, adivinadas)
        letras_limpias = " ".join(adivinadas)

    gano = ganador(adivinadas)
    if gano:
        os.system('cls')
        print(f'\t\t\tJuego de ahorcado\n\n\tvidas: {vidas}\tLetras encontradas: {letras_limpias}')
        print('\n\tFELICIDADES GANADOR!!!')
        os.system('pause')
        break

if vidas < 1:
    print(f'\n\tPerdiste la palabra era "{eleccion}"')
