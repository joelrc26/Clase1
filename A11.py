def main():
    """
    ## EJERCICIO 1
    numerosPares = []
    for x in range(0, 31):
        if x % 2 == 0:
            numerosPares.append(x)
    print(numerosPares)
    """
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
    for x in range(0, 1001):
        if '6' in str(x):
            numeros6.append(x)
    print(numeros6)
    """
    """
    ## EJERCICIO 4
    count = 0
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    for i in range(len(state)):
        if state[i] == " ":
            count += 1
    print("La frase tiene", count, "espacios")
    """
    """
    ## EJERCICIO 5
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    count = [i for i in state if i not in 'éaeiou ']
    print(count)
    """
    """
    ## EJERCICIO 6
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    count = [i for i in state.split() if len(i) < 5]
    print(count)
    """
if __name__ == '__main__':
        main()