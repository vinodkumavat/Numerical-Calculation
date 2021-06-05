import math

import Linear_Regression

import QE_regression


def RegressionDecider():
    print("After using this method always write the given data as it is")
    print("[0] -- y = summation (a_i*x_i)")
    print("[1] -- y = a*(e^bx)")
    print("[2] -- y = a*(x^b)")
    print("[3] -- y = a_0 + a_1*x + a_2*(x^2)")
    temp = int(input("\tWhich regression ==> "))
    return temp


def Input_0_Taker():
    # n = number of variable or parameter or features
    n = int(input("Enter the number of parameter or features ==> "))
    # m = number of equation or set
    m = int(input("Enter the number of equation or sets ==> "))
    X = []
    Y = []
    for i in range(m):
        print(f"\nEnter the value for {i+1} set ==> ")
        Set_i = []

        # 1st coloum must be alway 1 in X
        # Row indicate the set of values of parameter for 1st given set
        # Another row indicate the 2nd set of values of parameter for 2nd given set
        Set_i.append(1)
        for j in range(n):
            Set_i.append(float(input(f"\tEnter the Coefficient of A{j+1} of {i+1} set ==> ")))
        X.append(Set_i)
        Y.append(float(input(f"\tEnter the output of {i+1} set ==> ")))
    

    return X, Y, n, m


def Input_QE_Taker():
    # m = number of equation or set
    m = int(input("Enter the number of equation or sets ==> "))
    X = []
    Y = []
    for i in range(m):
        print(f"\nEnter the value for {i+1} set ==> ")

        X.append(float(input(f"\tEnter the value of x ==> ")))
        Y.append(float(input(f"\tEnter the value of Y({X[-1]}) ==> ")))
    
    

    print("\nGiven set of matrix is X ==> ")
    for i in range(m):
        print(X[i], end="\t")

    print("\nGiven output is Y ==> ")
    for i in range(m):
        print(Y[i])

    return X, Y


def normalLinear_1():
    X, Y, n, m = Input_0_Taker()
    Linear_Regression.LinearRegression(X, Y, n, m)


def exponential_2():
    # y = a*(e^bx)
    # lny = lna + b*x
    # Y = A0 + A1*x
    X, Y, n, m = Input_0_Taker()

    # need to log to the base e of y of each elements
    for i in range(len(Y)):
        Y[i] = math.log(Y[i])
    
    # calling linear_regression
    coefficient = Linear_Regression.LinearRegression(X, Y, n, m)
    # a = e^{A0}
    a = math.exp(coefficient[0])
    print(f"\n\nY(x) = a*(e^bx) = {a}*(e^({coefficient[1]})*x)")


def raisetopower_3():
    # y = a*(x^b)
    # logy = loga + b*logx
    # Y = A0 + A1*x

    X, Y, n, m = Input_0_Taker()
    
    # need to log to the base 10 of x and y of each elements
    for i in range(len(Y)):
        Y[i] = math.log10(Y[i])
        X[i][1] = math.log10(X[i][1])

    # calling linear_regression
    coefficient = Linear_Regression.LinearRegression(X, Y, n, m)
    # a = 10^{A0} and b = A1
    a = 10**coefficient[0]
    print(f"\n\nY(x) = a*(x^b) = {a}*(x^({coefficient[1]}))")


def Quadratic_4():
    X, Y = Input_QE_Taker()
    QE_regression.QERegression(X, Y)


def Runner():
    t = RegressionDecider()
    if t == 0:
        # normal linear regression
        normalLinear_1()
    if t == 1:
        # y = a*(e^bx)
        # lny = lna + b*x
        exponential_2()
    if t == 2:
        # y = a*(x^b)
        # logy = loga + b*logx
        raisetopower_3()
    if t == 3:
        Quadratic_4()

    print("Done")
        


Runner()