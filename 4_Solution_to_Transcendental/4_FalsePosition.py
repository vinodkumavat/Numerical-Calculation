# Same as Bisection formula just replace midPoint 
# by the point cut on x-axis by line joining two points
# also known as Regular False method
# It is also called as Bracketed method used when we know the boundary of solution
import math

def equation(x):
    # y(x) = 0
    y = math.exp(x) - 3
    return y


def limitChanger(x_l, x_u):
    y_l = equation(x_l)
    y_u = equation(x_u)
    x_r = (x_u*equation(x_l) - x_l*equation(x_u))/(equation(x_l) - equation(x_u))
    y_r = equation(x_r)

    if y_l*y_u > 0:
        print("Cannot find the root between [{x_l}, {x_u}]")
        return 0
    if y_l < 0 and y_u > 0:
        if y_r < 0:
            x_l = x_r
        if y_r > 0:
            x_u = x_r
    elif y_l > 0 and y_u < 0:
        if y_r < 0:
            x_u = x_r
        if y_r > 0:
            x_l = x_r
    return x_l, x_u


def Tablular(a, b, n):
    x_l = []
    y_l = []

    x_r = []
    y_r = []

    x_u = []
    y_u = []
    for i in range(n+1):
        x_l_temp, x_u_temp = limitChanger(a, b)
        x_r_temp = (b*equation(a) - a*equation(b))/(equation(a) - equation(b))
        # Inserting Upper and lower value
        x_l.append(a)
        y_l.append(equation(a))

        x_u.append(b)
        y_u.append(equation(b))

        # inserting middle value
        x_r.append(x_r_temp)
        y_r_temp = equation(x_r_temp)
        y_r.append(y_r_temp)

        # Changing the lower and upper value for next interation
        a = x_l_temp
        b = x_u_temp

    return x_l, y_l, x_r, y_r, x_u, y_u


def Caller():
    print(f"Make sure to update the equation function")
    a = float(input(f"Enter the initial value of x ==> "))
    b = float(input(f"Enter the final value of x ==> "))
    n = int(input(f"Enter the number of iteration ==> "))
    
    X_L, Y_L, X_R, Y_R, X_U, Y_U = Tablular(a, b, n)
    
    # Table printer
    Errorr = []
    Errorr.append("---")
    for i in range(n):
        err_temp = 100*((X_R[i+1] - X_R[i])/X_R[i+1])
        if err_temp < 0:
            Errorr.append(-err_temp)
        else:
            Errorr.append(err_temp)
        print(f"\n\nFor {i+1} iteration ==> ")
        print(f"\tX_L = {X_L[i]}")
        print(f"\tF(X_l) = F({X_L[i]}) = {Y_L[i]}")

        print(f"\tX_U = {X_U[i]}")
        print(f"\tF(X_u) = F({X_U[i]}) = {Y_U[i]}")

        print(f"\tX_R = {X_R[i]}")
        print(f"\tF(X_r) = F({X_R[i]}) = {Y_R[i]}")

        print(f"\tAbsolute_Error = {Errorr[i]}")


Caller()