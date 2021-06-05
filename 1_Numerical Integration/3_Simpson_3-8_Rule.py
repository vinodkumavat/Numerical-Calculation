#Simpson's 3/8 rule of integration
#num must be multiple of 3
#Assuming f(x) to be quadratic function
"""
Formula:-
    integration from a to b f(x) ==> Area ==>
        { 3*[b-a]/(8*n) } * { [f(a)] + [f(b)] + 2*[Summation (sum1) of f(a+h*i) from i=1 to i=n-1 for i mutliple of 3] + 3*[Summation (sum2) of f(a+h*i) from i=1 to i=n-1 for i which are not multiple of 3] }
    For Error calculation ==>
        True error = True value - Calculated Value
        Relative error = True error / True Value
"""

import math


def equation(x):
    #Definig Function y = 1000*sin(wt)*sin(wt) where w=100*pi
    y = (2000*math.log(140000/(140000 - 2100*x))) - 9.8*x
    return y


def Simpson_3_8(a, b, num):
    # Assuming b>a
    sum1 = 0
    sum2 = 0
    h = (b-a)/num
    
    # Print is just to solve the question
    print(f"Y({a}) ==> {equation(a)}, Y({b}) ==> {equation(b)}\n")

    for i in range(1, num):
        #3 multiple of i value of function summer
        if i%3 == 0:
            sum1 = sum1 + equation(a+(h*i))
            
            # Print is just to solve the question
            print(f"For 2*sum1 ==> Y({a+(h*i)}) ==> {equation(a+(h*i))}")
        #for rest of i's
        else:
            sum2 = sum2 + equation(a+(h*i))

            # Print is just to solve the question
            print(f"For 3*sum2 ==> Y({a+(h*i)}) ==> {equation(a+(h*i))}")

    # Print is just to solve the question
    print(f"\nSum1 ==> {sum1}, Sum2 ==> {sum2}\n")

    #For findind Area
    result = ((3*h)/8)*((2*sum1)+(3*sum2)+(equation(a))+(equation(b)))
    return result


def Caller():
    print("Make Sure, You have updated the equation function!")
    x0 = float(input("Enter the initial value of X ==> "))
    xn = float(input("Enter the final value of X ==> "))
    TrueValue = float(input(f"Enter the actual value for error calculation of integration ==> "))
    n = int(input("Enter the number of interval to be taken -- [Must be multiple of 3 ]- ==> "))

    print("Calculation is going on......\n")
    Area = Simpson_3_8(x0, xn, n)
    print(f"For n = {n}, Area = {Area}, True error = {TrueValue - Area}, %Relative error = {(100/TrueValue)*(TrueValue - Area)}")
    
    print("Thank You!")


Caller()