"""
    Formula:-
        Y(x) = a0 + a1*(x-x0) + a2*(x-x0)*(x-x1) + a3*(x-x0)(x-x1)*(x-x2) + ...........
        For coefficients a1, a2, a3, ........... use the newton tabular method
"""

def tableCalculator(X, Y, n):
    Result = []
    Result.append(Y)
    j_n = n
    for i in range(1, n+1):
        temp = []
        k = i
        for j in range(j_n):
            temp_j = (Result[i-1][j] - Result[i-1][j+1] )/ ( X[j] - X[k] )
            temp.append(temp_j)
            k = k + 1
        j_n = j_n - 1
        Result.append(temp)

    
    # Printing the Newton's Table
    print(f"\nNewton's Table of divided difference for order = {n}")
    for i in range(len(Result)):
        print(X[i], end= "\t")
        for j in range(len(Result[i])):
            print(Result[j][i], end="\t")
        print()

    return Result


def Coefficient(X, Y, n):
    # Return the vector containing the required coefficient only
    table_ = tableCalculator(X, Y, n)
    B = []
    print("\n\nRequire coeficients are:-")
    for i in range(len(table_)):
        B.append(table_[i][0])
        print(f"B{i} ==> {table_[i][0]}")
    return B


def Newton(X, Y, xn, n):
    B = Coefficient(X, Y, n)
    k = 1
    sum = 0
    print("\n\nValue of coefficient of coefficient:- ")
    for i in range(n+1):
        sum = sum + k*B[i]
        print(f"K{i} ==> {k}")
        k = k*(xn - X[i])
    
    print(f"\n\nFinal value ==> summation of (Bi)*(Ki) where i = [0, {n}]")
    print(f"Final value of Y({xn}) ==> {sum}")
    return sum


def Caller():
    print("Make sure you choice the correct points i.e. point near the values you need to find")
    n = int(input(f"Enter the order(degree) of polynomial ==> "))
    X = []
    Y = []

    for i in range(n+1):
        temp_x = float(input(f"Enter the value of x for {i+1} case ==> "))
        X.append(temp_x)
        temp_y = float(input(f"Enter the value of Y({temp_x}) ==> "))
        Y.append(temp_y)

    xn = float(input(f"Enter the value to find ==> "))


    result = Newton(X, Y, xn, n)

    # Printing result
    print(f"\nFor {n} order, Calculated value of Y({xn}) ==> {result}")  


Caller()