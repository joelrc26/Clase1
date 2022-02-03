
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

if __name__ == '__main__':
    main()