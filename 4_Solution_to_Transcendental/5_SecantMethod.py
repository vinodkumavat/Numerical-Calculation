# Secant need more iteration then newton raphson method
# but it is less then bisection
# Also known as Open bracket method are not known we solve by guessing the boundary
import math

def equation(x):
    # y(x) = 0 return function
    y = math.log(x**3) - x**2 + 5
    return y


def NewtonRaphson(x_1, x0, n):
    X = []
    Y_numer = []
    Y_deno = []
    X.append(x_1)
    X.append(x0)
    for i in range(n):
        y_numer_temp = equation(X[-1])*(X[-1] - X[-2])
        y_deno_temp = equation(X[-1]) - equation(X[-2])
        Y_numer.append(y_numer_temp)
        Y_deno.append(y_deno_temp)
        x_temp = X[-1] - (y_numer_temp / y_deno_temp)
        X.append(x_temp)
    return X, Y_numer, Y_deno


def Caller():
    print(f"Make sure to update the equation function")
    x0 = float(input(f"Enter the initial value of x [Choice such that derivative is defined]==> "))
    x_1 = float(input(f"X_[-1]==> "))
    n = int(input(f"Enter the number of iteration ==> "))
    
    X, Y, Y_der = NewtonRaphson(x_1, x0, n)
    
    # Table printer
    Errorr = []
    print("\n\nHere i in subscribe of X denote the i = iteration -1")
    for i in range(n):
        # index of X is +1 bcz we do not want the x_-1 part
        err_temp = 100*((X[i+2] - X[i+1])/X[i+2])
        if err_temp < 0:
            Errorr.append(-err_temp)
        else:
            Errorr.append(err_temp)
        print(f"\n\nFor {i+1} iteration ==> ")
        print(f"\tX_(i-1) = X_{i} ==> {X[i+1]}")

        print(f"\t\t[ Y(x_i)*[x_(i) - x_(i-1)] ] = {Y[i]}")
        print(f"\t\t[ Y[(x_i)] - Y[x_(i-1)] ] = {Y_der[i]}")
        print(f"\t\tRatio of above two terms = {Y[i]/Y_der[i]}")
        

        print(f"\tX_(i) = X_{i+1} ==> {X[i+2]}")        
        print(f"\tAbsolute_Error ==> {Errorr[i]}")

        print(f"\tY[x_(i+1)] = Y({X[i+2]}) ==> {equation(X[i+2])}")


Caller()
