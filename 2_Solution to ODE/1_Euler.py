"""
        ******** Euler-Method *********
Formula:-
    Y(i+1) = Y(i) + h*{ f(x(i), y(i)) }

"""

import math


def Derivative(x, y):
    # dy/dx
    deriv = (math.sin(x) - 5*y*y)*(1/3)
    return deriv


def Euler(x0, y0, xn, n):
    h = (xn-x0)/n
    y = y0
    for i in range(n):
        # Print is just to solve the question
        print(f"F({x0+i*h, y}) ==> {Derivative(x0+i*h, y)}")
        
        y = y + h*Derivative(x0+i*h, y)

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
    y = Euler(x0, y0, xn, n)
    print(f"For n = {n}, Calculated value of Y({xn}) ==> {y}, Relative Error ==> {(100*(y_actual-y))/y_actual}%")

    print("Thank You!")


Caller()