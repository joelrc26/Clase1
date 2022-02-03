def main():
    dia = int(input("Introduce el dia en el que naciste: "))
    while dia < 0 or dia > 31: # VALIDACION QUE EL DIA SEA MAYOR QUE 0 Y MENOR QUE 31
        dia = int(input("Introduce el dia en el que naciste: "))
    mes = int(input("Introduce el mes en el que naciste: "))
    while mes < 0 or mes > 12: # VALIDACION QUE EL MES SEA MAYOR QUE 0 Y MENOR QUE 13
        mes= int(input("Introduce el mes en el que naciste: "))
    año = int(input("Introduce el año en el que naciste: "))
    while año < 0: # VALIDACION QUE EL AÑO SEA MAYOR QUE 0
        año = int(input("Introduce el año en el que naciste: "))
    print("Data: ", dia, "-", mes, "-", año)
if __name__ == '__main__':
    main()