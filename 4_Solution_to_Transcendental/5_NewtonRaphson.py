# Used for non-linear equation and also for transcendental
# used when only one condition is given i.e. Y(x0) = Y0
# never take the extreme values as 
# Also known as Open bracket method were boundaries are not known we solve by guessing the boundary
import math
def equation(x, t):
    if t == 0:
        # y(x) = 0 return function
        y = math.exp(x) - 3
        return y
    elif t == 1:
        # y'(x) = 0 return derivative of function 
        y = math.exp(x)
        return y


def NewtonRaphson(x0, n):
    X = []
    Y = []
    Y_der = []
    X.append(x0)
    for i in range(n):
        y_temp = equation(X[-1], 0)
        y_deri_temp = equation(X[-1], 1)
        Y.append(y_temp)
        Y_der.append(y_deri_temp)
        x_temp = X[-1] - (y_temp / y_deri_temp)
        X.append(x_temp)
    return X, Y, Y_der


def Caller():
    print(f"Make sure to update the equation function")
    x0 = float(input(f"Enter the initial value of x [Choice such that derivative is defined]==> "))
    n = int(input(f"Enter the number of iteration ==> "))
    
    X, Y, Y_der = NewtonRaphson(x0, n)
    
    # Table printer
    Errorr = []
    for i in range(n):
        err_temp = 100*((X[i+1] - X[i])/X[i+1])
        if err_temp < 0:
            Errorr.append(-err_temp)
        else:
            Errorr.append(err_temp)
        print(f"\n\nFor {i+1} iteration ==> ")
        print(f"\tX_{i} = {X[i]}")
        print(f"\tY({X[i]}) = {Y[i]}")
        print(f"\tY'({X[i]}) = {Y_der[i]}")
        print(f"\tX_{i+1} = {X[i+1]}")
        print(f"\tAbsolute_Error = {Errorr[i]}")


Caller()
