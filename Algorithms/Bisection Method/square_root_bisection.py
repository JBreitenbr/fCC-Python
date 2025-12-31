"""
Implement the Bisection Method
The bisection method, also known as the binary search method, uses a binary search to find the roots of a real-valued function. It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

For example, if the tolerance is 0.01, the bisection method will keep halving the interval until the difference between the upper and lower bounds is less than or equal to 0.01.

In this lab, you will implement a function that uses the bisection method to find the square root of a number.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named square_root_bisection with three parameters:

The number for which you want to find the square root.
The tolerance being the acceptable error margin for the result. You should set a default tolerance value.
The maximum number of iterations to perform. You should set a default number of iterations.
The square_root_bisection function should:

Raise a ValueError with the message Square root of negative number is not defined in real numbers if the number passed to the function is negative.
For numbers 0 and 1, print the message: The square root of [number] is [number] and return the number itself as the square root.
For any other positive number, print the approximate square root with the message: The square root of [square_target] is approximately [root] and return the computed root value.
If no value meets the tolerance condition, print a failure message: Failed to converge within [maximum] iterations and return None.
"""

def square_root_bisection(num,tol=0.01,maxit=100):
    if num<0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif num==0 or num==1: 
        print(f"The square root of {num} is {num}")
        return num
    else:
        low=0
        if num<1:
            high=1
        else:
            high=num
    mid=(low+high)/2
    result=0
    for i in range(maxit):
        mid=(low+high)/2
        if (high-low)<=tol:
            break
        elif mid**2>num:
            high=mid
        else:
            low=mid
    result=mid
    if (high-low)<=tol:
        print(f"The square root of {num} is approximately {result}")
        return result
    else:
        print(f"Failed to converge within {maxit} iterations")
        return None
