"""
        ******** Runge_Kutta - 4th Order Method *********
Formula:-
    Y(i+1) = Y(i) + (h/6)*{k1 + k4 + 2*k2 + 2*k3}
        where
            k1 = f(x(i), y(i))
            k2 = f(x(i) + 0.5*h, Y(i) + 0.5*k1*h)
            k3 = f(x(i) + 0.5*h, Y(i) + 0.5*k2*h)
            k4 = f(x(i) + h, Y(i) + k3*h)

"""

import math


def Derivative(x, y):
    # dy/dx
    deriv = ((y**2) - (x**2))/((y**2) + (x**2))
    return deriv


def Runge_Kutta(x0, y0, xn, n):
    h = (xn-x0)/n
    y = y0
    for i in range(n):
        k1 = Derivative(x0+i*h, y)
        k2 = Derivative(x0+(i+0.5)*h, y+h*k1*0.5)
        k3 = Derivative(x0+(i+0.5)*h, y+k2*h*0.5)
        k4 = Derivative(x0+(i+1)*h, y+k3*h)

        # Print is just to solve the question
        print(f"At ({x0+h*i}, {y}) ==>")
        print(f"k1 ==> F({x0+h*i}, {y}) ==> {k1}")
        print(f"k2 ==> F({x0+(i+0.5)*h}, {y+h*k1*0.5}) ==> {k2}")
        print(f"k3 ==> F({x0+(i+0.5)*h}, {y+h*k2*0.5}) ==> {k3}")
        print(f"k4 ==> F({x0+(i+1)*h}, {y+h*k3}) ==> {k4}")

        y = y + (h/6)*(k1 + 2*(k2 + k3) + k4)

        # Print is just to solve the question
        print(f"Y({x0+h*(i+1)}) ==> {y}\n")
    return y


def Caller():
    print("Make Sure, You have updated the derivative function!")
    x0 = float(input("Enter the initial value of X ==> "))
    y0 = float(input(f"Enter the initial value of Y({x0}) ==> "))
    xn = float(input("Enter the final value of X ==> "))
    y_actual = float(input(f"Enter the actual value for error calculation of Y({xn}) ==> "))
    n = int(input("Enter the number of interval to be taken ==> "))

    print("Calculation is going on......\n")
    y = Runge_Kutta(x0, y0, xn, n)
    print(f"For n = {n}, Calculated value of Y({xn}) ==> {y}, Relative Error ==> {(100*(y_actual-y))/y_actual}%")

    print("Thank You!")


Caller()