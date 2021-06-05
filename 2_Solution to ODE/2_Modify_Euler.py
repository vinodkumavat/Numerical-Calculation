"""
        ******** Modify Euler-Method *********
Formula:-
    Predicted__Y(i+1) = Y(i) + h*{ f(x(i), y(i)) }
    Corrected__Y(i+1) = Y(i) + (h/2)*{ [ f(x(i), y(i)) ] + [ f(x(i+1), predicted__y(i+1)) ] }

"""

import math


def Derivative(x, y):
    # dy/dx
    deriv = (-2.2067*(10**-12))*(y**4 - (81*(10**8)))
    return deriv


def modify_Euler(x0, y0, xn, n):
    h = (xn-x0)/n
    y_predicted = y0
    y_corrected = y0
    for i in range(n):
        d1 = Derivative(x0+i*h, y_predicted)

        # Print is just to solve the question
        print(f"At ({x0+i*h, y_predicted}) ==>")
        print(f"F({x0+i*h, y_predicted}) ==> {Derivative(x0+i*h, y_predicted)}")

        y_predicted = y_predicted + h*d1

        # Print is just to solve the question
        print(f"Predicted Y({x0+h*(i+1)}) ==> {y_predicted}")
        print(f"F({x0+(i+1)*h, y_predicted}) ==> {Derivative(x0+(i+1)*h, y_predicted)}")

        y_corrected = y_corrected + 0.5*h*(d1 + Derivative(x0+(i+1)*h, y_predicted))

        # Print is just to solve the question
        print(f"Corrected Y({x0+h*(i+1)}) ==> {y_corrected}\n")

        y_predicted = y_corrected
    return y_corrected


def Caller():
    print("Make Sure, You have updated the derivative function!")
    x0 = float(input("Enter the initial value of X ==> "))
    y0 = float(input(f"Enter the initial value of Y({x0}) ==> "))
    xn = float(input("Enter the final value of X ==> "))
    y_actual = float(input(f"Enter the actual value for error calculation of Y({xn}) ==> "))
    n = int(input("Enter the number of interval to be taken ==> "))

    print("Calculation is going on......\n")
    y = modify_Euler(x0, y0, xn, n)
    print(f"For n = {n}, Calculated value of Y({xn}) ==> {y}, Relative Error ==> {(100*(y_actual-y))/y_actual}%")

    print("Thank You!")


Caller()