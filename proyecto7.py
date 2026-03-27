from random import randint
import os

class Persona():
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre:str, apellido:str, saldo:float, numero_cuenta:int):
        super().__init__(nombre, apellido)
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    # Metodo especial que le dice a mi nuevo objeto que hacer cuando se ponga en un print
    def __str__(self):
        return (f'Cliente: {self.nombre} {self.apellido},\nNumero de cuenta: {self.numero_cuenta},\nSaldo: {self.saldo}')
    
    def depositar(self, monto:float):
        self.saldo += monto
    
    def retirar(self, monto:float):
        self.saldo -= monto

    def checar_saldo(self):
        return (self.saldo)

def crear_numero_cuenta():
    cuentas_creadas = [10000000]
    num = 10000000
    while num in cuentas_creadas:
        num = randint(10000001, 99999999)
    cuentas_creadas.append(num)
    return num

def depositar(obj:Cliente):
    while True:
        monto = input('Ingresa la cantidad a depositar: ')
        if monto.isnumeric():
            monto = float(monto)
            if monto < 0:
                print('Opcion invalida')
            else:
                obj.depositar(monto)
                return obj
        else:
            print("Opcion invalida")

def retirar(obj:Cliente):
    while True:
        monto = input('Ingresa la cantidad a retirar: ')
        if monto.isnumeric():
            monto = float(monto)
            disponible = obj.checar_saldo()
            if monto > disponible:
                print('No tienes suficiente dinero!!')
            else:
                obj.retirar(monto)
                return obj
        else:
            print('Opcion invalida')

cajero_encedido = True
nombre = ''
apellido = ''
saldo = 0
while True:
    nombre = input('Ingresa un nombre: ')
    if nombre.isalpha() and len(nombre.split()) == 1:
        break
    else:
        print('Opcion invalida')
while True:
    apellido = input('Ingresa un apellido: ')
    if apellido.isalpha() and len(apellido.split()) == 1:
        break
    else:
        print('Opcion invalida')
while True:
    saldo = input('Ingresa el saldo de apertura de cuenta: ')
    if saldo.isnumeric():
        saldo = float(saldo)
        if  saldo >= 0:
            break
    else:
        print('Opcion invalida')
numero_cuenta = crear_numero_cuenta()
cliente1 = Cliente(nombre, apellido, saldo, numero_cuenta)

while cajero_encedido:
    os.system('cls')
    print('\tOpciones\t1. Retirar efectivo\t2. Depositar efectivo\t3. Salir\t')
    print(f'   Datos usuario \n{cliente1}')
    elecciones = ['1','2','3']
    while True:
        eleccion = input('Ingresa una opcion: ')
        if  eleccion in eleccion:
            if eleccion == '1':
                cliente1 = retirar(cliente1)
                break
            elif eleccion == '2':
                cliente1 = depositar(cliente1)
                break
            elif eleccion == '3':
                cajero_encedido = False
                print('Se apago el cajero')
                break
        else:
            print('Opcion invalida')

os.system('pause')
