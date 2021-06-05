#Simpson's 1/3 rule of integration
#num must be multiple of 2 i.e. even number
#Assuming f(x) to be quadratic function
"""
Formula:-
    integration from a to b f(x) ==> Area ==>
        { [b-a]/(3*n) } * { [f(a)] + [f(b)] + 4*[Summation (sum1) of f(a+h*i) from i=1 to i=n-1 for odd i] + 2*[Summation (sum2) of f(a+h*i) from i=2 to i=n-2 for even i] }
    For Error calculation ==>
        True error = True value - Calculated Value
        Relative error = True error / True Value
"""

import math


def equation(x):
    #Definig Function y = 1000*sin(wt)*sin(wt) where w=100*pi
    y = math.exp(x)
    return y


def Simpson_1_3(a, b, num):
    # Assuming b>a
    sum1 = 0
    sum2 = 0
    h = (b-a)/num

    # Print is just to solve the question
    print(f"Y({a}) ==> {equation(a)}, Y({b}) ==> {equation(b)}\n")

    for i in range(1, num):
        #Odd value of function summer
        if i%2 != 0:
            sum1 = sum1 + equation(a+(h*i))

            # Print is just to solve the question
            print(f"For 4*sum1 ==> Y({a+h*i}) ==> {equation(a+(h*i))}")

    for j in range(1, num-1):
        #Even value of function summer
        if j%2 == 0:
            sum2 = sum2 + equation(a+(h*j))

            # Print is just to solve the question
            print(f"For 2*sum2 ==> Y({a+h*j}) ==> {equation(a+(h*j))}")

    # Print is just to solve the question
    print(f"\nSum1 ==> {sum1}, Sum2 ==> {sum2}\n")

    #For findind Area
    result = (h/3)*((4*sum1)+(2*sum2)+(equation(a))+(equation(b)))
    return result


def Caller():
    print("Make Sure, You have updated the equation fucntion!")
    x0 = float(input("Enter the initial value of X ==> "))
    xn = float(input("Enter the final value of X ==> "))
    TrueValue = float(input(f"Enter the actual value for error calculation of integration==> "))
    n = int(input("Enter the number of interval to be taken -- [Must be Even number ]- ==> "))

    print("Calculation is going on......\n")
    Area = Simpson_1_3(x0, xn, n)
    print(f"For n = {n}, Area = {Area}, True error = {TrueValue - Area}, %Relative error = {(100/TrueValue)*(TrueValue - Area)}")
    
    print("Thank You!")


Caller()