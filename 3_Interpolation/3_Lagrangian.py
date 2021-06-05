"""
    Formula:-
        n = order of polynomial
        fn(x) = summation of    Li(x)*f(xi)     from    i=0 to n
        Li(x) = Product of      (x-xj)/(xi-xj)  from    j=0 to n except j=i
"""


def weightCalculator(X, xn, i):
    # Li(x)
    # n = (order of polynomial) + 1 = number of constant
    n = len(X)
    L_i = 1
    for j in range(n):
        if j != i:
            L_i = L_i*((xn-X[j])/(X[i] - X[j]))
            print(f"[({xn} - {X[j]})/({X[i]} - {X[j]})]", end=" * ")
    # Print is just to solve the question
    print(f"\nL{i}({xn}) ==> {L_i}\n")
    return L_i


def Lagrangian(X, Y, xn):
    # n = (order of polynomial) + 1 = number of constant
    n = len(X)
    f_x_i = 0
    for i in range(n):
        L_x_i = weightCalculator(X, xn, i)
        f_x_i = f_x_i + (L_x_i * Y[i])
    # Print is just to solve the question
    print(f"\nY({xn}) ==> {f_x_i}")
    return f_x_i


def Caller():
    print("Make sure you choice the correct points i.e. point near the values you need to find")
    n = int(input(f"Enter the order(degree) of polynomial ==> "))
    X = []
    Y = []

    for i in range(n+1):
        temp_x = float(input(f"Enter the value of x for {i+1} case ==> "))
        X.append(temp_x)
        temp_y = float(input(f"Enter the value of Y({temp_x}) ==> "))
        Y.append(temp_y)

    xn = float(input(f"Enter the value to find ==> "))

    # Print is just to solve the question
    print()

    result = Lagrangian(X, Y, xn)

    # Printing result
    print(f"\nFor {n} order, Calculated value of Y({xn}) ==> {result}")  


Caller()

