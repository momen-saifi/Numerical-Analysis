import math


def forward_diff(x, y, x0):
    n = len(x)
    forward_diff_table = [[0 for i in range(n)]
                          for j in range(n)]
    for i in range(n):
        forward_diff_table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            forward_diff_table[i][j] = (forward_diff_table[i + 1][j - 1] -
                                        forward_diff_table[i][j - 1])
    y0 = forward_diff_table[0][0]
    temp = 1
    for i in range(1, n):
        temp = temp * (x0 - x[i - 1])
        y0 += (forward_diff_table[0][i] * temp) / math.factorial(i)
    return y0



# Taking input from the user
n = int(input("Enter the number of data points: "))
x = []
y = []
for i in range(n):
    x_i = float(input(f"Enter the x-coordinate of data point {i+1}: "))
    y_i = float(input(f"Enter the y-coordinate of data point {i+1}: "))
    x.append(x_i)
    y.append(y_i)
x0 = float(input("Enter the x-coordinate at which to approximate the function value: "))


y0_forward = forward_diff(x, y, x0)

print(f"The approximate value of the function at x={x0} using Newton's forward differentiation formula is {y0_forward}")
