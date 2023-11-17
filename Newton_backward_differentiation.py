import numpy as np

def newton_backward_diff(x, y, x0):
    n = len(x)
    y = np.array(y)

    table = np.zeros((n, n))
    table[:,0] = y

    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = table[i+1][j-1] - table[i][j-1]

    h = x[1] - x[0]
    s = (x0 - x[-1]) / h

    res = table[-1][0]
    for i in range(1, n):
        p = 1
        for j in range(i):
            p *= (s + j)
        p /= np.math.factorial(i)
        res += p * table[-i-1][i]

    return res

n = int(input("Enter the number of data points: "))
x = np.array([float(input("Enter x{}: ".format(i))) for i in range(n)])

y = np.array([float(input("Enter y{}: ".format(i))) for i in range(n)])

x0 = float(input("Enter x to evaluate: "))

result_backward = newton_backward_diff(x, y, x0)
print(f"Interpolated value at {x0} using Newton's backward differentiation: {result_backward:.4f}")

