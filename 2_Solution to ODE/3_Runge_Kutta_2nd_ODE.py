"""
        ******** Runge_Kutta - 2nd Order Method *********
Methods derived from Runge_Kutta 2nd order method
    if a2 == 1/2:
        Heun's Method -- Best result obtained
    if a2 == 1:
        Midpoint Method
    if a2 = 2/3:
        Ralston's Method

Formula:-
    Y(i+1) = Y(i) + h*{a1*k1 + a2*k2}
        where
            a1 + a2 =1      (need to assume a2 for solving)
            p1*a2 = 1/2
            q11*a2 = 1/2
            k1 = f(x(i), y(i))
            k2 = f(x(i) + p1*h, Y(i) + q11*k1*h)

"""

import math


def Derivative(x, y):
    # dy/dx
    deriv = (-2.2067*(10**-12))*(y**4 - (81*(10**8)))
    return deriv


def Runge_Kutta(x0, y0, xn, n, a2):
    h = (xn-x0)/n
    y = y0
    a1 = 1 - a2
    p1 = 0.5/a2
    q11 = 0.5/a2
    for i in range(n):
        k1 = Derivative(x0+i*h, y)
        k2 = Derivative(x0+(i+p1)*h, y+q11*k1*h)

        # Print is just to solve the question
        print(f"At ({x0+h*i}, {y}) ==>")
        print(f"k1 ==> F({x0+h*i}, {y}) ==> {k1}")
        print(f"k2 ==> F({x0+(i+p1)*h}, {y+q11*k1*h}) ==> {k2}")

        y = y + h*(a1*k1 + a2*k2)

        # Print is just to solve the question
        print(f"Y({x0+h*(i+1)}) ==> {y}\n")
    return y


def Caller():
    print("Make Sure, You have updated the derivative function!")
    x0 = float(input("Enter the initial value of X ==> "))
    y0 = float(input(f"Enter the initial value of Y({x0}) ==> "))
    xn = float(input("Enter the final value of X ==> "))
    y_actual = float(input(f"Enter the actual value for error calculation of Y({xn}) ==> "))
    a2 = float(input("Enter the a2 value -[Must be less then 1]- a2 ==> "))
    n = int(input("Enter the number of interval to be taken ==> "))

    print("Calculation is going on......\n")
    y = Runge_Kutta(x0, y0, xn, n, a2)
    print(f"For n = {n}, Calculated value of Y({xn}) ==> {y}, Relative Error ==> {(100*(y_actual-y))/y_actual}%")

    print("Thank You!")


Caller()