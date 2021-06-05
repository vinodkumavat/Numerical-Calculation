import math


def OE(a, b, c):
    D = b**2 - 4*a*c
    root = -b/(2*a)
    if D == 0:
        print("Roots are equal and is ==> ")
        print(f"\tRoot = {root}")
        print(f"\tRoot = {root}")
    elif D > 0:
        alpha = root + (math.sqrt(D)/(2*a))
        beta = root - (math.sqrt(D)/(2*a))
        print("Roots are real and are ==> ")
        print(f"\talpha = {alpha}")
        print(f"\tbeta = {beta}")
    else:
        print("Roots are imaginary and are ==> ")
        print(f"\talpha = {root} + i {math.sqrt(-D)/(2*a)}")
        print(f"\tbeta = {root} - i {math.sqrt(-D)/(2*a)}")


def Caller():
    a = float(input(f"Enter the coefficient of x^2 ==> "))
    b = float(input(f"Enter the coefficient of x ==> "))
    c = float(input(f"Enter the constant coefficient ==> "))
    OE(a, b, c)


Caller()