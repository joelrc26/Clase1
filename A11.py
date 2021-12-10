def main():

    ## EJERCICIO 1
    numerosPares = []
    for x in range(0, 31):
        if x % 2 == 0:
            numerosPares.append(x)
    print(numerosPares)

    """
    ## EJERCICIO 2
    numeros8 = []
    for x in range(0, 1001):
        if x % 8 == 0:
            numeros8.append(x)
    print(numeros8)
    """
    """
    ## EJERCICIO 3
    numeros6 = []
    num = 1000
    for x in range(0, num + 1):
        if x == 6:
            numeros6.append(x)
    print(numeros6)
    """
if __name__ == '__main__':
        main()