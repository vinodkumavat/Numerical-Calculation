#Trapezoidal Rule of integration
#Assuming f(x) to be linear function
"""
Formula:-
    integration from a to b f(x) ==> Area ==>
        { [b-a]/(2*n) } * { [f(a)] + [f(b)] + 2*[Summation of f(a+h*i) from i=1 to i=n-1]}
    For Error calculation ==>
        True error = True value - Calculated Value
        Relative error = True error / True Value
"""

import math


def equation(x):
    #Definig intigral
    y = math.log(x)
    return y


def Trapezoidal(a, b, num):
    # Assuming b>a
    sum = 0
    h = (b-a)/num

    # Print is just to solve the question
    print(f"Y({a}) ==> {equation(a)}, Y({b}) ==> {equation(b)}\n")

    #For finding summation of f(a+ih)
    for i in range(1, num):
        sum = sum + equation(a+(h*i))

        # Print is just to solve the question
        print(f"For sum ==> Y({a+(h*i)}) ==> {equation(a+(h*i))}\n")

    # Print is just to solve the question
    print(f"Sum = {sum}\n")

    #For findind value = { [b-a]/[2*num] }*{ [2*summation] + [f(a)] + [f(b)] }
    result = (h/2)*((2*sum)+(equation(a))+(equation(b)))
    return result


def Caller():
    print("Make Sure, You have updated the equation function!")
    x0 = float(input("Enter the initial value of X ==> "))
    xn = float(input("Enter the final value of X ==> "))
    TrueValue = float(input(f"Enter the actual value for error calculation of integration ==> "))
    n = int(input("Enter the number of interval to be taken ==> "))

    print("Calculation is going on......\n")
    Area = Trapezoidal(x0, xn, n)
    print(f"For n = {n}, Area = {Area}, True error = {TrueValue - Area}, %Relative error = {(100/TrueValue)*(TrueValue - Area)}")
    
    print("Thank You!")


Caller()