from random import randint
#import os

vidas = 8
nombre = input('Ingresa el nombre del jugador: ')
random = randint(1, 100)
gano = False

def revisar_num(intento, vidas, random):
    if intento > 100 or intento < 1:
        print('Numero invalido!!')
        return vidas
    elif intento > random:
        print('Te pasaste')
        return vidas - 1
    elif intento < random:
        print('Te falto')
        return vidas - 1
    else:
        return vidas

def ganador(intento, random):
    if intento == random:
        return True
    else:
        return False

while vidas > 0:
    #os.system('cls')
    print(f'\n\tJugador {nombre}\tvidas: {vidas}')
    intento = int(input('Ingresa un numero entre el 1 y el 100: '))
    vidas = revisar_num(intento, vidas, random)
    gano = ganador(intento, random)
    if gano:
        print('QUE BARBARO PANA!!!')
        break

if vidas < 1:
        print('HAS PERDIO CHAVALO!!!')
        print(f'El numero era {random}')
