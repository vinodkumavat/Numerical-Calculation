"""
        ******** Runge_Kutta - 2nd Order Method for higher ODE*********
                                Valid for 2nd order DE
Formula:-
    dy/dx = f1(x(i), y(i), z(i))
    d2y/dx2 = dz/dx = f2(x(i), y(i), z(i))
    
    Y(i+1) = Y(i) + 0.5*h*{k1_y + k2_y}
    Z(i+1) = Z(i) + 0.5*h*{k1_z + k2_z}
        where
            k1_y = f1(x(i), y(i), z(i))
            k1_z = f2(x(i), y(i), z(i))
            k2_y = f1(x(i) + h, Y(i) + k1_y*h, z(i) + k1_z*h)
            k2_z = f2(x(i) + h, Y(i) + k1_y*h, z(i) + k1_z*h)

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


def Runge_Kutta(x0, y0, z0, xn, n):
    h = (xn-x0)/n
    y = y0
    z = z0
    for i in range(n):
        k1_y = Derivative(x0+i*h, y, z, 1)
        k1_z = Derivative(x0+i*h, y, z, 2)
        k2_y = Derivative((x0+(i+1)*h), (y+k1_y*h), (z+k1_z*h), 1)
        k2_z = Derivative((x0+(i+1)*h), (y+k1_y*h), (z+k1_z*h), 2)

        # Print is just to solve the question
        print(f"At ({x0+h*i}, {y}) ==>")
        print(f"k1_y ==> F1({x0+h*i}, {y}, {z}) ==> {k1_y}")
        print(f"k1_z ==> F2({x0+h*i}, {y}, {z}) ==> {k1_z}")
        print(f"k2_y ==> F1({x0+(i+1)*h}, {y+k1_y*h}, {z+k1_z*h}) ==> {k2_y}")
        print(f"k2_z ==> F2({x0+(i+1)*h}, {y+k1_y*h}, {z+k1_z*h}) ==> {k2_z}")

        y = y + 0.5*h*(k1_y + k2_y)
        z = z + 0.5*h*(k1_z + k2_z)

        # Print is just to solve the question
        print(f"Y({x0+h*(i+1)}) ==> {y}")
        print(f"Z({x0+h*(i+1)}) ==> {z}\n\n")
    return y


def Caller():
    print("Make Sure, You have updated the derivative function!")
    x0 = float(input("Enter the initial value of X ==> "))
    y0 = float(input(f"Enter the initial value of Y({x0}) ==> "))
    xn = float(input("Enter the final value of X ==> "))
    z0 = float(input(f"Enter the initial value of dy/dx| x={x0} ==> "))
    y_actual = float(input(f"Enter the actual value for error calculation of Y({xn}) ==> "))
    n = int(input("Enter the number of interval to be taken ==> "))

    print("Calculation is going on......\n")
    y = Runge_Kutta(x0, y0, z0, xn, n)
    print(f"For n = {n}, Calculated value of Y({xn}) ==> {y}, Relative Error ==> {(100*(y_actual-y))/y_actual}%")

    print("Thank You!")


Caller()