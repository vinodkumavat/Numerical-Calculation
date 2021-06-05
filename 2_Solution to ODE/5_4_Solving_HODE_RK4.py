"""
        ******** Runge_Kutta - 4th Order Method (NOT Verified) *********
                                Valid for 2nd order DE
Formula:-
    Y(i+1) = Y(i) + (h/6)*{k1 + k4 + 2*k2 + 2*k3}
        where
            k1_y = f1(x(i), y(i), z(i))
            k1_z = f2(x(i), y(i), z(i))

            k2_y = f1(x(i) + 0.5*h, Y(i) + 0.5*k1_y*h, Z(i) + 0.5*k1_z*h)
            k2_z = f2(x(i) + 0.5*h, Y(i) + 0.5*k1_y*h, Z(i) + 0.5*k1_z*h)

            k3_y = f1(x(i) + 0.5*h, Y(i) + 0.5*k2_y*h, Z(i) + 0.5*k2_z*h)
            k3_z = f2(x(i) + 0.5*h, Y(i) + 0.5*k2_y*h, Z(i) + 0.5*k2_z*h)

            k4_y = f1(x(i) + h, Y(i) + k3_y*h, Z(i) + k3_z*h)
            k4_z = f2(x(i) + h, Y(i) + k3_y*h, Z(i) + k3_z*h)

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


def Runge_Kutta(x0, y0, z0, xn, n):
    h = (xn-x0)/n
    y = y0
    z = z0
    for i in range(n):
        k1_y = Derivative(x0+i*h, y, z, 1)
        k1_z = Derivative(x0+i*h, y, z, 2)

        k2_y = Derivative(x0+(i+0.5)*h, y+h*k1_y*0.5, z+0.5*k1_z*h, 1)
        k2_z = Derivative(x0+(i+0.5)*h, y+h*k1_y*0.5, z+0.5*k1_z*h, 2)

        k3_y = Derivative(x0+(i+0.5)*h, y+h*k2_y*0.5, z+0.5*k2_z*h, 1)
        k3_z = Derivative(x0+(i+0.5)*h, y+h*k2_y*0.5, z+0.5*k2_z*h, 2)

        k4_y = Derivative(x0+(i+1)*h, y+k3_y*h, z+k3_z*h, 1)
        k4_z = Derivative(x0+(i+1)*h, y+k3_y*h, z+k3_z*h, 2)


        # Print is just to solve the question
        print(f"At ({x0+h*i}, {y}) ==>")
        print(f"k1_y ==> F1({x0+h*i}, {y}, {z}) ==> {k1_y}")
        print(f"k1_z ==> F2({x0+h*i}, {y}, {z}) ==> {k1_z}")

        print(f"k2_y ==> F1({x0+(i+0.5)*h}, {y+h*k1_y*0.5}, {z+0.5*k1_z}) ==> {k2_y}")
        print(f"k2_z ==> F2({x0+(i+0.5)*h}, {y+h*k1_y*0.5}, {z+0.5*k1_z}) ==> {k2_z}")

        print(f"k3_y ==> F1({x0+(i+0.5)*h}, {y+h*k2_y*0.5}, {z+0.5*k2_z}) ==> {k3_y}")
        print(f"k3_z ==> F2({x0+(i+0.5)*h}, {y+h*k2_y*0.5}, {z+0.5*k2_z}) ==> {k3_z}")

        print(f"k4_y ==> F1({x0+(i+1)*h}, {y+k3_y*h}, {z+k3_z}) ==> {k4_y}")
        print(f"k4_z ==> F2({x0+(i+1)*h}, {y+k3_y*h}, {z+k3_z}) ==> {k4_z}")


        y = y + (h/6)*(k1_y + 2*(k2_y + k3_y) + k4_y)
        z = z + (h/6)*(k1_z + 2*(k2_z + k3_z) + k4_z)


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