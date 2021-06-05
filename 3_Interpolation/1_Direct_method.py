"""
    Formula:-
        Y(x) = a0 + a1*x + a2*(x**2) + a3*(x**3) + ........ + an*(x**n)
        
        Example:- 2nd order
            Given:-     t       10          15          20
                        V(t)    227.04      362.78      517.35
            To find:- V(16) = ?
            Solution
                    Y(t) = a0 + a1*t + a2*t*t
                    matrix X ==>    |1  10  100|        Matrix A ==>    |a0|    Matrix Y ==>    |227.04|
                                    |1  15  225|                        |a1|                    |362.78|    
                                    |1  20  400|                        |a2|                    |517.35|
                    Y(t) == [Matrix X] * [Matrix A] = [Matrix Y]
                    need to matrix A
                    [Matrix A] = (inverse[Matrix X])*[Matrix Y]
                    Y(16) = a0 + a1*16 + a2*16*16
"""

import numpy


def parameterCalculator(X, Y):
    # XA = Y where X ==> mxn matrix with m=number of sets available, n=number of features
    # A = (inverse(X))*Y
    X_inverse = numpy.linalg.inv(X)
    # multiplication
    A = numpy.dot(X_inverse, Y)
    return A


def directMethod(x0, X, Y):
    A = parameterCalculator(X, Y)

    # Print is just to solve the question
    print(f"\nParamateres are A (inv(X)*Y)==> ")

    sum_ = 0
    for i in range(len(A)):
        # Print is just to solve the question
        print(f"a_{i} = {A[i]}")
        sum_ = sum_ + A[i]*(x0**(i))
    return sum_


def Caller():
    print("Make sure you choice the correct points i.e. point near the values you need to find")
    n = int(input(f"Enter the order(degree) of polynomial ==> "))
    X = []
    Y = []

    for i in range(n+1):
        row_elements = []
        x_i = float(input(f"Enter the value of x for {i+1} case ==> "))
        y_i = float(input(f"Enter the value of Y({x_i}) ==> "))
        for j in range(n+1):
            row_elements.append(x_i**j)
        X.append(row_elements)
        Y.append(y_i)
    x0 = float(input(f"Enter the value to find ==> "))

    # Printing matrix just to solve the question
    print(f"\nMatrix X ==> ")
    for i in range(len(X)):
        for j in range(len(X[0])):
            print(X[i][j], end="\t")
        print()
    print(f"\nMatrix Y ==> ")
    for i in range(len(Y)):
        print(Y[i])

    # Calling For Calculation
    y0 = directMethod(x0, X, Y)

    # Printing result
    print(f"\nFor {n} order, Calculated value of Y({x0}) ==> {y0}")


Caller()