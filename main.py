def main():
    """
## EJERCICIO MESES CON IF
    mes = str(input("Introduce un mes del año: "))
    if mes == "Febrero":
        print("El mes introducido tiene 28 días")
    elif mes == "Abril" or mes == "Junio" or mes == "Septiembre" or mes == "Noviembre":
        print("El mes introducido tiene 30 días")
    else:
        print("El mes introducido tiene 31 días")
    """
"""
    ## EJERCICIO MESES CON MATCHCASE
mes = int(input("Introduce un mes del año: "))
while mes < 1 or mes > 12:
    mes = int(input("Introduce un mes del año: "))
match mes:
    case 1:
        print("Has introducido el mes de Enero.\nTiene 31 dias")
    case 2:
        print("Has introducido el mes de Febrero.\nTiene 28 dias")
    case 3:
        print("Has introducido el mes de Marzo.\nTiene 31 dias")
    case 4:
        print("Has introducido el mes de Abril.\nTiene 30 dias")
    case 5:
        print("Has introducido el mes de Mayo.\nTiene 31 dias")
    case 6:
        print("Has introducido el mes de Junio.\nTiene 30 dias")
    case 7:
        print("Has introducido el mes de Julio.\nTiene 31 dias")
    case 8:
        print("Has introducido el mes de Agosto.\nTiene 31 dias")
    case 9:
        print("Has introducido el mes de Septiembre.\nTiene 30 dias")
    case 10:
        print("Has introducido el mes de Octubre.\nTiene 31 dias")
    case 11:
        print("Has introducido el mes de Noviembre.\nTiene 30 dias")
    case 12:
        print("Has introducido el mes de Diciembre.\nTiene 31 dias")
"""
"""
    ## EJERCICIO QUE INTERCAMBIA DOS NUMEROS ENTEROS
num1 = int(input("Introduce un numero que despues su valor sera intercambiado\n"))
while num1 < 0:
    num1 = int(input("Introduce un numero que despues su valor sera intercambiado\n"))
    num2 = int(input("Introduce otro numero que despues su valor sera intercambiado con el anterior\n"))
while num2 < 0:
    num2 = int(input("Introduce otro numero que despues su valor sera intercambiado con el anterior\n"))
aux = num1
num1 = num2
num2 = aux
print("Valores intercambiados:", num1, num2)
"""
"""
    ## EJERCICIO VALIDAR SI ES NUMERO NATURAL
num1 = int(input("Introduce un número natural: "))
while num1 < 1:
    num1 = int(input("Introduce un número natural: "))
print("El número introducido", [num1] ," es un número natural")
"""
"""
    ## EJERCICIOS CONVERSIÓN DE GRADOS
FARENHEIT = 32.00
KELVIN = 273.15
print("MENÚ")
print("1. Convertir de grados Celsius a grados Farenheit")
print("2. Convertir de grados Celsius a grados Kelvin")
print("3. Salir")
menu = int(input("Introduce un número del menú: "))
while menu >= 4:
    menu = int(input("Introduce un número del menú: "))
    grados = int(input("Introduce la temperatura en ºC: "))
match menu:
    case 1:
        grados = grados + FARENHEIT
        print("La conversión es:", grados, "grados Farenheit")
    case 2:
        grados = grados + KELVIN
        print("La conversión es:", grados, "grados Kelvin")
"""
"""
    ## EJERCICIO SUMA
num = int(input("Introduce un número: "))
resultado, suma = 0, 0
while num < 0:
    num = int(input("Introduce un número: "))
while num >= resultado + suma:
    resultado = suma + resultado
    print(suma, "->", resultado)
    suma += 1
"""
"""
## EJERCICIO MOSTRAR PALABRAS AL REVÉS
print((input("Introduce tu frase: ")[::-1]))
"""
"""
## EJERCICIO PARA AÑADIR VALORES A UNA LISTA
print("Si el usuario introduce un 0 la lista se mostrará")
lista = []
lista.append(str(input("Introduce valores que quieras añadir a la lista: ")))
print(lista)
"""
"""
## EJERCICIO NOMBRE Y APELLIDOS
name = str(input("Introduce tu nombre: "))
firstname = str(input("Introduce el primer apellido: "))
lastname = str(input("Introduce el segundo apellido: "))
print(firstname[:2] + lastname[:2] + name[:2])
"""
"""
## EJERCICIO LISTA CON INFO
lista1 = []
lista2 = []
lista3 = []
lista4 = []
users = int(input("Introduce cuantos registros quieres introducir: "))
while users < 0:
    users = int(input("Introduce cuantos registros quieres introducir: "))

for x in range(users):
    name = input("Introduce el nombre: ")
    firstname = input("Introduce el primer apellido: ")
    lastname = input("Introduce el segundo apellido: ")
    lista1.append(firstname[:2] + lastname[:2] + name[:2])
    telephone = input("Introduce el número de teléfono: ")
    lista2.append(telephone)
    age = int(input("Introduce la edad: "))
    while age < 0:
        age = int(input("Introduce la edad: "))
    lista3.append(age)
    contact = int(input("Introduce si ha tenido contacto (1) o no (0): "))
    lista4.append(contact)
print("Codi     Telèfon     Edat   Contacte ")
for x in range(users):
    print(lista1[x], end="   ")
    print(lista2[x], end="   ")
    print(lista3[x], end="     ")
    print(lista4[x])
"""
"""
## INTERVALO DE NÚMEROS
print("Introduce dos números siendo n1 < n2")
n1 = int(input("Introduce un número para n1: "))
n2 = int(input("Introduce un número para n2: "))
while n2 < n1:
    n1 = int(input("Introduce un número para n1: "))
    n2 = int(input("Introduce un número para n2: "))
for x in range(n1, n2 + 1):
    print(x)
"""
"""
## NOTAS Y MEDIAS
approved, failed = 0, 0
resultA, resultF = 0, 0
mediaA, mediaF = 0, 0
num = int(input("Introduce cuantas notas vas a introducir: "))
while num < 0:
    num = int(input("Introduce cuantas notas vas a introducir: "))
for x in range(num):
    notes = int(input("Introduce la nota del alumno: "))
    while notes < 0 or notes > 10:
        notes = int(input("La nota que has introducido es menor que 0 o mayor que 10, introduce otra diferente: "))
    if notes < 5:
        failed += 1
        resultF += notes
    else:
        approved += 1
        resultA += notes
mediaF = resultF / failed
mediaA = resultA / approved
print("Cantidad de Aprobados: ", approved)
print("Media de los Aprobados: ", mediaA)
print("Cantidad de Suspensos: ", failed)
print("Media de los Suspensos: ", mediaF)
"""
"""
## ESTRUCTURA GESTIÓN USUARIOS
header = ['Username', 'Department', 'Classroom']
username = list()
dept = list()
classroom = list()
registres = int(input("Introduce los registros que quieras añadir: "))
for i in range(registres):
    username.append(input("Introduce el nombre de usuario "))
    dept.append(input("Introduce el departamento: "))
    classroom.append(int(input("Introduce la clase: ")))
regs = {
    "username": username,
    "dept": dept,
    "classroom": classroom
}
for i in header:
    print(i, end="\t|")
print()
for i in range(registres):
    print(regs['username'][i] + '\t\t|' + regs['department'][i] + '\t\t|' + str(regs['classroom'][i]) + '\t\t |')
"""

## EJERCICIO 33
count = 0
letra = str(input("Introduce una letra: "))
arrayNotes = 'a', 'z', 'g', 'd', 'w', 'o', 'h', 'e', 'x', 's'
for i in arrayNotes:
    if i == letra:
        count = 1
if count == 1:
    print("La letra introducida", [letra], "está en el array")
else:
    print("La letra introducida", [letra], "NO está en el array")

if __name__ == '__main__':
    main()