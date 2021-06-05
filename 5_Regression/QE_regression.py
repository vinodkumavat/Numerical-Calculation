# MEthod name --> Least square method
# Assuming y = a_0* + a_1*(x) + a_2*(x^2)

import numpy


def SummationMatrix(X):
    # X = input i.e. it will be array

    element_11 = len(X)
    
    element_12_21 = 0
    for i in range(len(X)):
        element_12_21 = element_12_21 + X[i]

    element_13_22_31 = 0
    for i in range(len(X)):
        element_13_22_31 = element_13_22_31 + (X[i]**2)

    element_23_32 = 0
    for i in range(len(X)):
        element_23_32 = element_23_32 + (X[i]**3)
    
    element_33 = 0
    for i in range(len(X)):
        element_33 = element_33 + (X[i]**4)
    
    Result = []
    # inserting row 1
    Result.append([element_11, element_12_21, element_13_22_31])

    # inserting row 2
    Result.append([element_12_21, element_13_22_31, element_23_32])

    # inserting row 3
    Result.append([element_13_22_31, element_23_32, element_33])
    
    # Printing the matrix
    print("\nSummation matrix is ==> ")
    for i in range(len(Result)):
        for j in range(len(Result[0])):
            print(Result[i][j], end="\t")
        print()

    return Result


def OutputMatrix(X, Y):
    # n = number of variable or parameter or features
    # m = number of equation or set
    Output_Y = []
    for i in range(3):
        temp = 0
        for k in range(len(Y)):
            temp = temp + Y[k]*(X[k]**i)
        Output_Y.append(temp)
    
    # Print
    print("\nOutput matrix Y ==> ")
    for i in range(len(Output_Y)):
        print(Output_Y[i])

    return Output_Y


def CoefficientMatrix(X, Y):
    # n = number of variable or parameter or features
    # m = number of equation or set

    summation_X = SummationMatrix(X)
    output_Y = OutputMatrix(X, Y)

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


def QERegression(X, Y):
    A = CoefficientMatrix(X, Y)

    print("\n\nFinal equation is ==> ")
    print(f"Y(x) = ({A[0]}) + ({A[1]})*x + ({A[2]})*x^2")
