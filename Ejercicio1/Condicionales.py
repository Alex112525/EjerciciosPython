def evennumber(num):
    if num%2 == 0:
        print("Numero par")
    else:
        print("Numero impar")


def primenumber(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        print("numero primo")
    elif num%2 == 0 or num%3 == 0 or num%5 ==0 or num%7 == 0:
        print("Numero no primo")
    else:
        print("numero primo")


def leapday(year):
    leap = False
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
    return leap


def number(num):
    if num == 0:
        print("Tu numero es cero")
    elif num > 0:
        print("Numero positivo")
    elif num < 0:
        print("Numero negativo")


if __name__ == "__main__":
    n = int(input("Introduce un numero \n"))
    number(n)
    primenumber(n)
    evennumber(n)

    year = int(input("Introduce un año \n"))
    if leapday(year):
        print("Año bisiesto")
    else:
        print("Año no bisiesto")
