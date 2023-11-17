import numpy
def divided_difference(x, y, n):
    """Calculate divided differences for Newton's Interpolation"""
    table = [0] * (n + 1)
    for i in range(n + 1):
        table[i] = [0] * (n + 1)
    for i in range(n + 1):
        table[i][0] = y[i]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            table[i][j] = (table[i][j - 1] - table[i - 1][j - 1]) / (x[i] - x[i - j])
    return table[n]

def newton_interpolation(x_values, y_values, x, n):
    """Return the value of the polynomial at x using Newton's Interpolation"""
    result = y_values[0]
    for i in range(1, n + 1):
        term = divided_difference(x_values, y_values, i)[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term
    return result

n = int(input("Enter the number of data points: "))

x_values = numpy.array([float(input("Enter x{}: ".format(i))) for i in range(n)])

y_values = numpy.array([float(input("Enter y{}: ".format(i))) for i in range(n)])

x = float(input("Enter x to evaluate: "))

result = newton_interpolation(x_values, y_values, x, n - 1)
print("Result:", result)
