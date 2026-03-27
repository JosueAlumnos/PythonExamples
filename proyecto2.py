name = str(input("Cual es tu nombre? "))
sale = int(input("Cuanto vendiste? "))

def calc_salary(value):
    return(value * 0.13)

def main():
    return print(f'Hola {name}\nvendiste {sale} por lo que tu comision es {round(calc_salary(sale), 2)}')

main()