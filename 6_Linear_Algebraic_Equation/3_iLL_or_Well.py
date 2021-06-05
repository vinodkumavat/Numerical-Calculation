# Required only coefficient matrix

from numpy import linalg
import math


def InputTaker():
    # n = number of variable or parameter or features or equations
    n = int(input("Enter the order of square matrix ==> "))
    X = []
    # Taking equation
    for i in range(n):
        print(f"\nEnter the value for {i+1} row ==> ")
        Set_i = []

        for j in range(n):
            Set_i.append(float(input(f"\tEnter the elements of {j+1} Coloum, {i+1} Row ==> ")))
        X.append(Set_i)

    print("\nGiven matrix is ==> ")
    for i in range(n):
        for j in range(n):
            print(X[i][j], end="\t")
        print()

    return X


def ill_well(A):
    # Determinant of A = _A_
    _A_ = linalg.det(A)
    print(f"\nDeterminant of matrix is = {_A_}")

    # S[i] = magnitude of row vector
    S = []
    for i in range(len(A)):
        sum_ = 0
        for j in range(len(A[0])):
            sum_ = sum_ + A[i][j]**2
        S.append(math.sqrt(sum_))
        print(f"S_{i+1} ==> sqrt({sum_}) ==> {S[i]}")
        _A_ = _A_/S[i]
    print(f"K = {_A_}")
    if _A_ < 0:
        _A_ = -_A_
    print(f"\nModulus of K = |K| = {_A_}")
    print("\n\n*** Always check if :- ***\n\t|K| is near 1 ==> It is well condition\n\t|K| <<<<< 1 ==> It is ill condition")

    if round(_A_) == 1:
        print(f"\nAs |K|= {_A_} is near 1, it is well condition.")
    else:
        print(f"\nAs |K| = {_A_} is very less then 1, it is ill condition")


def Caller():
    A = InputTaker()
    ill_well(A)

    
Caller()