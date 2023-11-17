
def runge_kutta(f, x0, y0, h, xn):
    n = int((xn - x0) / h) + 1
    x = [0] * n
    y = [0] * n
    x[0] = x0
    y[0] = y0
    for i in range(n - 1):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + k1/2)
        k3 = h * f(x[i] + h/2, y[i] + k2/2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
        x[i+1] = x[i] + h
    return x, y


print("Enter the differential equation in the form y' = f(x, y)")
f_str = input("f(x, y) = ")


f = lambda x, y: eval(f_str)

x0 = float(input("Enter the initial value of x: "))
y0 = float(input("Enter the initial value of y: "))
xn = float(input("Enter the final value of x: "))
h = float(input("Enter the step size: "))

x, y = runge_kutta(f, x0, y0, h, xn)


for i in range(len(x)):
    print(f"x = {x[i]:.4f}, y = {y[i]:.4f}")
