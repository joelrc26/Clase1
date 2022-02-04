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

if __name__ == '__main__':
    main()