# Newton's Raphson --> for 2 variable --> Using Jacobinian method
# Only for 2 equation with 2 unknown

import numpy


def derivative(x, y):
    # d[ f(x, y) ]/ dx 
    f_x = 2*x
    # d[ f(x, y) ]/ dy 
    f_y = -2*y

    # d[ g(x, y) ]/ dx 
    g_x = 2*x
    # d[ g(x, y) ]/ dy
    g_y = 2*y

    F = []
    F.append(f_x)
    F.append(f_y)

    G = []
    G.append(g_x)
    G.append(g_y)

    J = []
    J.append(F)
    J.append(G)

    # Print
    print("\n\tJacobian Matrix J ==> ")
    for i in range(len(J)):
        for j in range(len(J[0])):
            print(f"\t{J[i][j]}", end="\t")
        print()
    return J


def equation(x, y):
    Y = []
    F = x**2 - y**2 - 4
    G = x**2 + y**2 - 16
    Y.append(-F)
    Y.append(-G)

    # Print
    print("\n\tMatrix Y ==> ")
    for i in range(len(Y)):
        print(f"\t{Y[i]}")
    return Y


def coefficient(x, y):
    J = derivative(x, y)
    Y = equation(x, y)
    # A = (inverse(X))*Y
    J_inverse = numpy.linalg.inv(J)
    # multiplication
    A = numpy.dot(J_inverse, Y)

    # Print
    print("\n\tCoefficient Matrix A ==> ")
    for i in range(len(A)):
        print(f"\t{A[i]}")

    print("\n\tNew (x, y) ==> ")
    print(f"\t({A[0]+x}, {A[1] + y})")
    return A


def Caller():
    print(f"Make sure to update the equation and derivative function")
    x0 = float(input(f"Enter the initial value of x ==> "))
    y0 = float(input(f"Enter the initial value of y ==> "))
    n = int(input(f"Enter the number of iteration ==> "))
    X = []
    Y = []
    X.append(x0)
    Y.append(y0)
    for i in range(n):
        print(f"\nFor the {i+1} iteration")
        print(f"\tWith initial condition ==> \n\t\t({X[-1]}, {Y[-1]})")
        A = coefficient(X[-1], Y[-1])
        X.append(A[0] + X[-1])
        Y.append(A[1] + Y[-1])
    print("Done")


Caller()
