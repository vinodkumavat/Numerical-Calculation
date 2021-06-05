"""
        ******** Modify Euler-Method for Higher ODE (Not Verified) *********

Formula:-
    Predicted__Y(i+1) = Y(i) + h*{ f1(x(i), y(i)) }
    Predicted__Z(i+1) = Z(i) + h*{ f2(x(i), y(i)) }

    Corrected__Y(i+1) = Y(i) + (h/2)*{ [ f1(x(i), y(i)) ] + [ f1(x(i+1), predicted__Y(i+1)) ] }
    Corrected__Z(i+1) = Z(i) + (h/2)*{ [ f2(x(i), y(i)) ] + [ f2(x(i+1), predicted__Z(i+1)) ] }

"""

import math


def Derivative(x, y, z, temp):
    # temp return the required Derivative on bases of demand
    # dy/dx = f1(x, y, z)
    f1 = z
    
    # d2y/dx2 == dz/dx = Double derivative == f2(x, y, z)
    f2 = math.exp(-x)-2*z-y

    if temp == 1:
        return f1
    if temp == 2:
        return f2


def modify_Euler(x0, y0, z0, xn, n):
    h = (xn-x0)/n
    y_predicted = y0
    z_predicted = z0
    y_corrected = y0
    z_corrected = z0
    for i in range(n):
        d1 = Derivative(x0+i*h, y_predicted, z_predicted, 1)
        d2 = Derivative(x0+i*h, y_predicted, z_predicted, 2)

        # Print is just to solve the question
        print(f"At ({x0+i*h}, {y_predicted}) ==>")
        print(f"F1({x0+i*h}, {y_predicted}, {z_predicted}) ==> {Derivative(x0+i*h, y_predicted, z_predicted, 1)}")
        print(f"F2({x0+i*h}, {y_predicted}, {z_predicted}) ==> {Derivative(x0+i*h, y_predicted, z_predicted, 2)}")

        y_predicted = y_predicted + h*d1
        z_predicted = z_predicted + h*d2

        # Print is just to solve the question
        print(f"Predicted Y({x0+h*(i+1)}) ==> {y_predicted}")
        print(f"Predicted Z({x0+h*(i+1)}) ==> {z_predicted}")
        print(f"F1({x0+(i+1)*h, y_predicted, z_predicted}) ==> {Derivative(x0+(i+1)*h, y_predicted, z_predicted, 1)}")
        print(f"F2({x0+(i+1)*h, y_predicted, z_predicted}) ==> {Derivative(x0+(i+1)*h, y_predicted, z_predicted, 2)}")

        y_corrected = y_corrected + 0.5*h*(d1 + Derivative(x0+(i+1)*h, y_predicted, z_predicted, 1))
        z_corrected = z_corrected + 0.5*h*(d2 + Derivative(x0+(i+1)*h, y_predicted, z_predicted, 2))

        # Print is just to solve the question
        print(f"Corrected Y({x0+h*(i+1)}) ==> {y_corrected}")
        print(f"Corrected Z({x0+h*(i+1)}) ==> {z_corrected}\n\n")

        y_predicted = y_corrected
        z_predicted = z_corrected
    return y_corrected


def Caller():
    print("Make Sure, You have updated the derivative function!")
    x0 = float(input("Enter the initial value of X ==> "))
    y0 = float(input(f"Enter the initial value of Y({x0}) ==> "))
    xn = float(input("Enter the final value of X ==> "))
    z0 = float(input(f"Enter the initial value of dy/dx| x={x0} ==> "))
    y_actual = float(input(f"Enter the actual value for error calculation of Y({xn}) ==> "))
    n = int(input("Enter the number of interval to be taken ==> "))

    print("Calculation is going on......\n")
    y = modify_Euler(x0, y0, z0, xn, n)
    print(f"For n = {n}, Calculated value of Y({xn}) ==> {y}, Relative Error ==> {(100*(y_actual-y))/y_actual}%")

    print("Thank You!")


Caller()