import numpy as np


# Newton's forward interpolation with initial approximation
def newton_forward_interpolation(x, y, x0):
    n = len(x)
    y = np.array(y)

    # calculate the forward difference table
    table = np.zeros((n, n))
    table[:,0] = y

    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = table[i+1][j-1] - table[i][j-1]

    # calculate the interpolated value at x0
    h = x[1] - x[0]
    s = (x0 - x[0]) / h

    res = y[0]
    for i in range(1, n):
        p = 1
        for j in range(i):
            p *= (s - j)
        p /= np.math.factorial(i)
        res += p * table[0][i]

    return res

# sample data

n = int(input("Enter the number of data points: "))
x = np.array([float(input("Enter x{}: ".format(i))) for i in range(n)])

y = np.array([float(input("Enter y{}: ".format(i))) for i in range(n)])

x0 = float(input("Enter x to evaluate: "))

# interpolate using Newton's forward interpolation with initial approximation
result_forward = newton_forward_interpolation(x, y, x0)
print(f"Interpolated value at {x0} using Newton's forward interpolation: {result_forward:.4f}")
