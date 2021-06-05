"""
        ******** Euler-Method for Higher ODE*********
            Valid for 2nd order DE
Formula:-
    dy/dx = f1(x(i), y(i), z(i))
    d2y/dx2 = dz/dx = f2(x(i), y(i), z(i))
    Y(i+1) = Y(i) + h*{ f1(x(i), y(i)) }
    Z(i+1) = Z(i) + h*{ f2(x(i), y(i)) }

"""

import math


def Derivative(x, y, z, temp):
    # temp return the required Derivative on bases of demand
    # dy/dx = f1(x, y, z)
    f1 = z
    
    # d2y/dx2 == dz/dx = Double derivative == f2(x, y, z)
    f2 = math.exp(-x) - y - 2*z

    if temp == 1:
        return f1
    if temp == 2:
        return f2
    
    

def Euler(x0, y0, z0, xn, n):
    h = (xn-x0)/n
    y = y0
    z = z0
    for i in range(n):
        # Print is just to solve the question
        print(f"At x = {x0+h*(i+1)}")
        print(f"F1({x0+i*h, y, z}) ==> {Derivative(x0+i*h, y, z, 1)}")
        print(f"F2({x0+i*h, y, z}) ==> {Derivative(x0+i*h, y, z, 2)}")
        
        y_temp = y + h*Derivative(x0+i*h, y, z, 1)
        z_temp = z + h*Derivative(x0+i*h, y, z, 2)
        z = z_temp
        y = y_temp

        # Print is just to solve the question
        print(f"Y({x0+h*(i+1)}) ==> {y}")
        print(f"Z({x0+h*(i+1)}) ==> {z}\n")
    return y, z


def Caller():
    print("Make Sure, You have updated the derivative function!")
    x0 = float(input("Enter the initial value of X ==> "))
    y0 = float(input(f"Enter the initial value of Y({x0}) ==> "))
    xn = float(input("Enter the final value of X ==> "))
    z0 = float(input(f"Enter the initial value of dy/dx| x={x0} ==> "))
    y_actual = float(input(f"Enter the actual value for error calculation of Y({xn}) ==> "))
    n = int(input("Enter the number of interval to be taken ==> "))

    print("Calculation is going on......\n")
    y, z = Euler(x0, y0, z0, xn, n)
    print(f"For n = {n}, Calculated value of Y({xn}) ==> {y}, Calculated dy/dx at {xn} ==> {z}, Relative Error for Y({xn}) ==> {(100*(y_actual-y))/y_actual}%")

    print("Thank You!")


Caller()