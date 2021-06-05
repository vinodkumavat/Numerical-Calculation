# It is also called as Bracketed method used when we know the boundary of solution
import math
def equation(x):
    # y(x) = 0
    y = math.exp(x) - 3
    return y


def limitChanger(x_l, x_u):
    y_l = equation(x_l)
    y_u = equation(x_u)
    x_m = (x_l + x_u)/2
    y_m = equation(x_m)

    if y_l*y_u > 0:
        print("Cannot find the root between [{x_l}, {x_u}]")
        exit()
    if y_l < 0 and y_u > 0:
        if y_m < 0:
            x_l = x_m
        if y_m > 0:
            x_u = x_m
    elif y_l > 0 and y_u < 0:
        if y_m < 0:
            x_u = x_m
        if y_m > 0:
            x_l = x_m
    return x_l, x_u


def Tablular(a, b, n):
    x_l = []
    y_l = []

    x_m = []
    y_m = []

    x_u = []
    y_u = []
    for i in range(n+1):
        x_l_temp, x_u_temp = limitChanger(a, b)
        # Inserting Upper and lower value
        x_l.append(a)
        y_l.append(equation(a))

        x_u.append(b)
        y_u.append(equation(b))

        # inserting middle value
        x_m.append((a+b)/2)
        y_m_temp = equation((a+b)/2)
        y_m.append(y_m_temp)

        # Changing the lower and upper value for next interation
        a = x_l_temp
        b = x_u_temp

    return x_l, y_l, x_m, y_m, x_u, y_u


def Caller():
    print(f"Make sure to update the equation function")
    a = float(input(f"Enter the initial value of x ==> "))
    b = float(input(f"Enter the final value of x ==> "))
    n = int(input(f"Enter the number of iteration ==> "))
    
    X_L, Y_L, X_M, Y_M, X_U, Y_U = Tablular(a, b, n)
    
    # Table printer
    Errorr = []
    Errorr.append("---")
    for i in range(n):
        err_temp = 100*((X_M[i+1] - X_M[i])/X_M[i+1])
        if err_temp < 0:
            Errorr.append(-err_temp)
        else:
            Errorr.append(err_temp)
        print(f"\n\nFor {i+1} iteration ==> ")
        print(f"\tX_L = {X_L[i]}")
        print(f"\tF(X_l) = F({X_L[i]}) = {Y_L[i]}")

        print(f"\tX_U = {X_U[i]}")
        print(f"\tF(X_u) = F({X_U[i]}) = {Y_U[i]}")

        print(f"\tX_M = {X_M[i]}")
        print(f"\tF(X_m) = F({X_M[i]}) = {Y_M[i]}")

        print(f"\tAbsolute_Error = {Errorr[i]}")

    
Caller()