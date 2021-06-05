# Diagonal elements must be non-zero
# Updating the variables after one complete interation


def equation(X, Y, Result):
    temp = []
    for i in range(len(Y)):
        sum_ = 0
        for j in range(len(Y)):
            if i != j:
                sum_ = sum_ + X[i][j]*Result[j]
        temp.append((Y[i] - sum_)/X[i][i])
    # updating after one complete iteration and storing as array
    Result = temp
    return Result


def InputTaker():
    # n = number of variable or parameter or features or equations
    n = int(input("Enter the number of parameter or features ==> "))
    X = []
    Y = []
    # Taking equation
    for i in range(n):
        print(f"\nEnter the value for {i+1} set ==> ")
        Set_i = []

        for j in range(n):
            Set_i.append(float(input(f"\tEnter the Coefficient of X{j+1} of {i+1} set ==> ")))
        X.append(Set_i)
        Y.append(float(input(f"\tEnter the output of {i+1} set ==> ")))


    # Taking initial condition
    Result = []
    print("\nEnter the initial conditions")
    for i in range(n):
        Result.append(float(input(f"\tEnter the initial value of X{i+1} ==> ")))

    n_iteration = int(input("\nEnter the number of iteration ==> "))
    

    print("\nGiven Coefficient matrix X ==> ")
    for i in range(n):
        for j in range(n):
            print(X[i][j], end="\t")
        print()
    print("\nGiven output is Y ==> ")
    for i in range(n):
        print(Y[i])

    return X, Y, Result, n, n_iteration


def ConvergenceTest(X):
    # Considering the modulus of elements
    diagonal_elements = []
    rest_elements_sum = []
    for i in range(len(X)):
        sum_ = 0
        for j in range(len(X[0])):
            # Making all elements positive
            t = X[i][j]
            if  t < 0:
                t = -t
            if i == j :
                diagonal_elements.append(t)
            else:
                sum_ = sum_ + t
        rest_elements_sum.append(sum_)
    
    # Now comparing for dominant diagonal element or not
    # count_1 for |each diagonal elements| >= |sum of rest of elemts|
    # count_2 for atleast one row |each diagonal elements| > |sum of rest of elemts|
    count_1 = 0
    count_2 = 0
    for i in range(len(diagonal_elements)):
        if diagonal_elements[i] >= rest_elements_sum[i]:
            count_1 = count_1 + 1
        if diagonal_elements[i] > rest_elements_sum[i]:
            count_2 = count_2 + 1
    # Conclusion
    if count_1 == len(diagonal_elements):
        if count_2 >=1:
            print("\n\nGiven matrix will converge")
    else:
        print("\n\nGiven matrix do not converge.\nTry inchanging the row")
        exit()


def Jacobi():
    # n = number of variable or parameter or features or equations
    # n_iteration = number of iteration to be done
    X, Y, Result, n, n_iteration = InputTaker()

    # Tasting for convergence 
    ConvergenceTest(X)

    # Printing table
    print("\n\nItertn", end="\t\t")
    for j in range(n):
        print(f"X_{j+1}", end="\t\t")
    for i in range(n_iteration+1):
        print(f"\n{i}", end="\t\t")
        for j in range(n):
            print(f"{round(Result[j], 5)}", end="\t\t")
        Result = equation(X, Y, Result)
    print()
    
    # for i in range(n_iteration+1):
    #     print(f"\n\nFor {i} iteration ==> ")
    #     for j in range(n):
    #         print(f"\tX_{j+1} = {Result[j]}")
    #     Result = equation(X, Y, Result)


Jacobi()