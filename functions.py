"""
# EJERCICIO 1
def validate():
    count = 0
    num = int(input("Introdueix un nombre que estigui entre el 10 i el 5000: "))
    while (num < 10 or num > 5000) and count < 2:
        num = int(input("Introdueix un nombre que estigui entre el 10 i el 5000: "))
        count = count + 1
    if count == 2:
        return -1
    else:
        return num
def main():
    num1 = validate()
    while num1 == -1:
        print("Te has equivocado 3 veces")
        num1 = validate()
    print("Has introducido el ", num1)
"""
"""
# EJERCICIO 2
def validate():
    num = int(input("Escribe el número total de segundos: "))
    while num < 0:
        num = int(input("Escribe el número total de segundos: "))
    return num

def main():
    seconds = validate()
    hours = seconds // 3600
    minutes = seconds // 60
    if minutes == 60:
        minutes = 0
        seconds = seconds // 60
    if seconds == 60:
        seconds = 0
    print("Equivalen a ", hours, "horas, ", minutes, "minutos y ", seconds, "segundos")
"""
"""
# EJERCICIO 3
def validate():
    num = int(input("Introdueix un nombre enter: "))
    while num < 0:
        num = int(input("Introdueix un nombre enter: "))
    return num

def main():
    count = 1
    rem = binary = 0
    num1 = validate()
    while num1 != 0:
        rem = num1 % 2
        num1 = num1 // 2
        binary = binary + (rem * count)
        count = count * 10
    print("La conversio a binari és: ", binary)
"""
"""
# EJERCICIO 4
def validate():
    num = int(input("Introduce una nota: "))
    while num < 0 or num > 10:
        num = int(input("Introduce una nota: "))
    return num

def main():
    count = approved = failed = 0
    mediaA = mediaF = resultA = resultF = 0
    print("********* INTRODUCE 15 NOTAS *********\n")
    while count < 15:
        nota = validate()
        if nota >= 5:
            approved += 1
            resultA += nota
        else:
            failed += 1
            resultF += nota
        count = count + 1
        print("Llevas puestas", count, "notas de 15")
    mediaA = resultA / approved
    mediaF = resultF / failed
    print("La cantidad de aprobados son: ", approved)
    print("La cantidad de suspensos son: ", failed)
    print("La nota media de los que han aprobado es un: ", mediaA)
    print("La nota media de los que han suspendido es un: ", mediaF)
"""
"""
# EJERCICIO 5
def validate():
    num = int(input("Introduce un numero el cual después su valor será intercambiado: "))
    while num < 0:
        num = int(input("Introduce un numero el cual después su valor será intercambiado: "))
    return num
def main():
    num1 = validate()
    num2 = validate()
    print("Valores antes de intercambiarse: ", num1, num2)
    num1, num2 = num2, num1
    print("Valores intercambiados: ",num1, num2)
"""
"""
# EJERCICIO 6
def validate():
    num = int(input("Introduce un número mayor que 0: "))
    while num < 0:
        num = int(input("Introduce un número mayor que 0: "))
    return num

def comprobar(num):
    sum = count = 0
    while sum <= num:
        sum = sum + count
        if sum <= num:
            print(count)
            count = count + 1
    print("El resultado de la suma es:")
    return sum - count

def main():
    num = validate()
    print(comprobar(num))
"""
"""
# EJERCICIO 7

"""
"""
# EJERCICIO 8
def validateE():
    exp = int(input("Introduce un número de exponente: "))
    while exp < 0:
        exp = int(input("Introduce un número de exponente: "))
    return exp

def validate():
    base = int(input("Introduce un número de base: "))
    while base < 0:
        base = int(input("Introduce un número de base: "))
    return base

def main():
    result = count = 1
    base = validate()
    exp = validateE()
    while (count <= exp):
        result = result * base
        count = count + 1
    print("El resultado de la operación es igual a:", result)
"""
"""
# EJERCICIO 9

"""

# EJERCICIO 10
def validate():
    num = int(input("Introduce el numero de libros que vas a introducir: "))
    while num < 1:
        num = int(input("Introduce el numero de libros que vas a introducir: "))
    return num

def main():
    count = 1
    num = validate()
    for x in range(num):
        print("\n------------------------------ INTRODUCE LOS DATOS DEL LIBRO", count, "------------------------------")
        DatosLibro = {'Titulo del libro: ': input("Introduce el titulo del libro: "),
                      'Autor del libro: ': input("Introduce el autor del libro: "),
                      'Editorial del libro: ': input("Introduce la editorial del libro: "),
                      'Dia de publicación: ': int(input("Introduce el dia de publicación: ")),
                      'Mes de publicación: ': int(input("Introduce el mes de publicación: ")),
                      'Año de publicación: ': int(input("Introduce el año de publicación: ")),
                      'Número de unidades disponibles: ': int(input("Introduce el número de unidades disponibles: ")),
                      'Usuario que tiene el préstamo del libro: ': input(
                          "Introduce el usuario que tiene el préstamo del libro: "),
                      'Tiempo de préstamo en dias: ' : int(input("Introduce el tiempo de préstamo en dias: "))
                      }
        print("\n---------------------------------- DATOS DEL LIBRO", count, "----------------------------------")
        for x in DatosLibro:
            print(x, DatosLibro[x])
        count = count + 1

if __name__ == '__main__':
    main()