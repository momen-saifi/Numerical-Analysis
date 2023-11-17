import numpy as np
from sympy import Symbol, lambdify, integrate

def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a) / n
    return (h/2) * (y[0] + 2*np.sum(y[1:n]) + y[n])

def simpsons_one_third_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a) / n
    sum1 = np.sum(y[1:n:2])
    sum2 = np.sum(y[2:n-1:2])
    return (h/3) * (y[0] + 4*sum1 + 2*sum2 + y[n])


expr = input("Enter a function in x: ")
x = Symbol('x')
f = lambdify(x, expr)


a = float(input("Enter lower limit of integration: "))
b = float(input("Enter upper limit of integration: "))
n = int(input("Enter number of subintervals: "))


trapezoidal_result = trapezoidal_rule(f, a, b, n)



print(f"The result using Trapezoidal Rule is: {trapezoidal_result:.6f}")

