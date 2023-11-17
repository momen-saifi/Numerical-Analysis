import numpy 

def lagrange_interpolation(x, y, x_eval):

    n = len(x)
    result = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x_eval - x[j]) / (x[i] - x[j])
        result += y[i] * Li
    return result


n = int(input("Enter the number of data points: "))
x = numpy.array([float(input("Enter x{}: ".format(i))) for i in range(n)])

y = numpy.array([float(input("Enter y{}: ".format(i))) for i in range(n)])

x_eval = float(input("Enter x to evaluate: "))

result = lagrange_interpolation(x, y, x_eval)
print("Result:", result)
