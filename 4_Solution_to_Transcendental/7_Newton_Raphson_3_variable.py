# Newton's Raphson --> for 3 variable --> Using Jacobinian method
# Only for 3 equation with 3 unknown

import numpy


def derivative(x, y, z):
    # F1(x, y, z) = 0
    # For 1st function f1(x, y, z)
    # d[ f1(x, y, z) ]/ dx 
    f_1_x = 2*x - 2
    # d[ f1(x, y, z) ]/ dy 
    f_1_y = 2*y
    # d[ f1(x, y, z) ]/ dz 
    f_1_z = -1

    # For 2nd function f2(x, y, z)
    # d[ f2(x, y, z) ]/ dx 
    f_2_x = y**2 - 1
    # d[ f2(x, y, z) ]/ dy 
    f_2_y = 2*x*y - 3 + z
    # d[ f2(x, y, z) ]/ dz 
    f_2_z = y

    # For 3rd function f3(x, y, z)
    # d[ f3(x, y, z) ]/ dx 
    f_3_x = z**2 + y
    # d[ f3(x, y, z) ]/ dy 
    f_3_y = z**2 + x
    # d[ f3(x, y, z) ]/ dz 
    f_3_z = 2*x*z - 3 + 2*y*z


    F1 = []
    F1.append(f_1_x)
    F1.append(f_1_y)
    F1.append(f_1_z)

    F2 = []
    F2.append(f_2_x)
    F2.append(f_2_y)
    F2.append(f_2_z)

    F3 = []
    F3.append(f_3_x)
    F3.append(f_3_y)
    F3.append(f_3_z)

    J = []
    J.append(F1)
    J.append(F2)
    J.append(F3)

    # Print
    print("\n\tJacobian Matrix J ==> ")
    for i in range(len(J)):
        for j in range(len(J[0])):
            print(f"\t{J[i][j]}", end="\t")
        print()
    return J


def equation(x, y, z):
    Y = []
    # F(x, y, z) = 0
    F1 = x**2 - 2*x + y**2 - z + 1
    F2 = x*(y**2) - y - 3*y + y*z + 2
    F3 = x*(z**2) - (3*z) + y*(z**2) + x*y
    Y.append(-F1)
    Y.append(-F2)
    Y.append(-F3)

    # Print
    print("\n\tMatrix Y ==> ")
    for i in range(len(Y)):
        print(f"\t{Y[i]}")
    return Y


def coefficient(x, y, z):
    J = derivative(x, y, z)
    Y = equation(x, y, z)
    # A = (inverse(X))*Y
    J_inverse = numpy.linalg.inv(J)
    # multiplication
    A = numpy.dot(J_inverse, Y)

    # Print
    print("\n\tCoefficient Matrix A ==> ")
    for i in range(len(A)):
        print(f"\t{A[i]}")

    print("\n\tNew (x, y, z) ==> ")
    print(f"\t({A[0]+x}, {A[1] + y}, {A[2] + z})")
    return A


def Caller():
    print(f"Make sure to update the equation and derivative function")
    x0 = float(input(f"Enter the initial value of x ==> "))
    y0 = float(input(f"Enter the initial value of y ==> "))
    z0 = float(input(f"Enter the initial value of z ==> "))
    n = int(input(f"Enter the number of iteration ==> "))
    X = []
    Y = []
    Z = []
    X.append(x0)
    Y.append(y0)
    Z.append(z0)
    for i in range(n):
        print(f"\nFor the {i+1} iteration")
        print(f"\tWith initial condition ==> \n\t\t({X[-1]}, {Y[-1]}, {Z[-1]})")
        A = coefficient(X[-1], Y[-1], Z[i])
        X.append(A[0] + X[-1])
        Y.append(A[1] + Y[-1])
        Z.append(A[2] + Z[-1])
    print("Done")


Caller()
