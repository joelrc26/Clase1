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

if __name__ == '__main__':
    main()