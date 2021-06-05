
from numpy import math as np

def tableCalculator(X, Y, n):
    Result = []
    Result.append(Y)
    j_n = n
    for i in range(1, n+1):
        temp = []
        for j in range(j_n):
            temp_j = Result[i-1][j+1] - Result[i-1][j]
            temp.append(temp_j)
        j_n = j_n - 1
        Result.append(temp)

    
    # Printing the Newton's Table
    print(f"\nNewton's Table of divided difference for order = {n}")
    for i in range(len(Result)):
        for j in range(len(Result[i])):
            print(Result[j][i], end="\t")
        print()

    return Result


def ForwardCoefficient(X, Y, n):
    # Return the vector containing the required coefficient only
    table_ = tableCalculator(X, Y, n)
    FC = []
    print("\n\nRequire Forward coeficients are:-")
    for i in range(len(table_)):
        FC.append(table_[i][0])
        print(f"(∆^{i})y_0 ==> {table_[i][0]}")
    return FC


def BackwardCoefficient(X, Y, n):
    # Return the vector containing the required coefficient only
    table_ = tableCalculator(X, Y, n)
    BC = []
    print("\n\nRequire Backward coeficients are:-")
    for i in range(len(table_)):
        BC.append(table_[i][-1])
        print(f"(∇^{i})y_{n} ==> {table_[i][-1]}")
    return BC


def ForwardCaller(X, Y, xn, n):
    h = X[1] - X[0]
    p = (xn - X[0]) / h
    temp_p = p
    print(f"h(steps taken) ==> {h}, p ==> {p}")
    FC = ForwardCoefficient(X, Y, n)
    k = 1
    sum = 0
    print("\n\nValue of coefficient of coefficient(i.e function of p excluding factorial term):- ")
    for i in range(n+1):
        sum = sum + (k*FC[i]/(np.factorial(i)))
        print(f"P{i} ==> {k}")
        k = (k*temp_p)
        temp_p = temp_p - 1
    print(f"\n\nFinal value ==> summation of ((∆^i)y_0)*(Pi)/(i!) where i = [0, {n}]")
    print(f"Final value of Y({xn}) ==> {sum} by Forward newton method")
    return sum


def BackwardCaller(X, Y, xn, n):
    h = X[1] - X[0]
    p = (xn - X[-1]) / h
    temp_p = p
    print(f"h(steps taken) ==> {h}, p ==>({xn} - {X[-1]})/{h} = {p}")
    BC = BackwardCoefficient(X, Y, n)
    k = 1
    sum = 0
    print("\n\nValue of coefficient of coefficient(i.e function of p excluding factorial term):- ")
    for i in range(n+1):
        sum = sum + (k*BC[i]/(np.factorial(i)))
        print(f"P{i} ==> {k}")
        k = (k*temp_p)
        temp_p = temp_p + 1
    print(f"\n\nFinal value ==> summation of (∇^i)_y{n}))*(Pi)/(i!) where i = [0, {n}]")
    print(f"Final value of Y({xn}) ==> {sum} by Backward newton method")
    return sum


def Newton(X, Y, xn, n, temp):
    if temp == 0:
        # Forward Newton's Difference interpolation
        return ForwardCaller(X, Y, xn, n)

    if temp == 1:
        # Backward Newton's Difference interpolation
        return BackwardCaller(X, Y, xn, n)


def Caller():
    print("Make sure you enter the value of X for fixed interval i.e. values after every each h steps")
    n = int(input(f"Enter the order(degree) of polynomial ==> "))
    x0 = float(input(f"Enter the initial value of X ==> "))
    h = float(input(f"Enter the step size for X i.e h ==> "))
    X = []
    Y = []

    for i in range(n+1):
        temp_y = float(input(f"Enter the value of Y({x0}) ==> "))
        Y.append(temp_y)
        X.append(x0)
        x0 = x0 + h

    xn = float(input(f"Enter the value to find ==> "))
    decide = int(input(f"[0] - Forward Newton's\n[1] - Backward Newton's\nEnter the value ==> "))

    result = Newton(X, Y, xn, n, decide)

    # Printing result
    print(f"\nFor {n} order, Calculated value of Y({xn}) ==> {result}")  


Caller()