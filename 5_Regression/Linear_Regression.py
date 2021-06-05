# MEthod name --> Least square method
# For multi variable variable
# Assuming y = summation (ai*xi)
# Can be used for non-linear of type :- y = ax^b and y = ae^bx
# by taking log and they will be linear in logy, logx and lny and x

# instead of using this file use Adequacy.py

import numpy


def SummationMatrix(X, n, m):
    # n = number of variable or parameter or features
    # m = number of equation or set
    Result = []
    for i in range(n+1):
        temp_coloum = []
        for j in range(n+1):
            temp = 0
            for k in range(m):
                temp = temp + X[k][j]*X[k][i]
            temp_coloum.append(temp)
        Result.append(temp_coloum)

    # Printing the matrix
    print("\nSummation matrix is ==> ")
    for i in range(n+1):
        for j in range(n+1):
            print(Result[i][j], end="\t")
        print()

    return Result


def OutputMatrix(X, Y, n, m):
    # n = number of variable or parameter or features
    # m = number of equation or set
    Output_Y = []
    for i in range(n+1):
        temp = 0
        for k in range(m):
            temp = temp + Y[k]*X[k][i]
        Output_Y.append(temp)
    
    # Print
    print("\nOutput matrix Y ==> ")
    for i in range(len(Output_Y)):
        print(Output_Y[i])

    return Output_Y


def CoefficientMatrix(X, Y, n, m):
    # n = number of variable or parameter or features
    # m = number of equation or set

    summation_X = SummationMatrix(X, n, m)
    output_Y = OutputMatrix(X, Y, n, m)

    # XA = Y where X ==> mxn matrix with m=number of sets available, n=number of features
    # A = (inverse(X))*Y
    X_inverse = numpy.linalg.inv(summation_X)
    # multiplication
    A = numpy.dot(X_inverse, output_Y)

    # print 
    print("\nCoeffient matrix is ==> ")
    for i in range(len(A)):
        print(f"A{i} = {A[i]}")
        
    return A


def LinearRegression(X, Y, n, m):
    # n = number of variable or parameter or features
    # m = number of equation or set
    # printing the input given by user
    print("\nGiven set of matrix is X ==> ")
    for i in range(m):
        for j in range(n+1):
            print(X[i][j], end="\t")
        print()
    print("\nGiven output is Y ==> ")
    for i in range(m):
        print(Y[i])
    A = CoefficientMatrix(X, Y, n, m)
    return A

