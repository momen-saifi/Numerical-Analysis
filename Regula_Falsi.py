from sympy import symbols, lambdify
import math


    
def funRF():
    
    x = symbols('x')
    equation = str(input("Enter the function in the form \'x**3 + 4*x**2 - 10\': "))
    f = lambdify(x, equation)
    a = int(input("If you want to enter intervel press 1 outherwise press 2 "))


    if(a==2):
        
           
        for i in range(-10,10):   
            r1=i
            r2=i+1
            if(f(r1)*f(r2)<0):
                x1=r1
                x2=r2
            
         
            
            
            
            
    if (a==1):

        table = []
        for i in range(-10, 10):
            table.append((i,f(i)))
        print("x\tf(x)")
        for x,y in table:
            print(f"{x}\t{y}")
   
       
        while True:
            x1 = float(input("Enter the first guess intervel: "))
            x2 = float(input("Enter the second guess intervel: "))
            if (f(x1) * f(x2) < 0):
                print("Root lies in the interval")
                break
            else:
                print("No Root between the given points ({0},{1}). Please choose another pair of starting points.".format(x1,x2))
                print("Enter the intervals again\n")
        
    pos = float(input("Enter the desired Precision in the form of\'0.00001\': "))

    count = 0
    x3 = 0.0
   

    print("\nIterations\tx1\t\tx2\t\tx3\t\tf(x3)")
    while (abs(f(x3))> pos) :
        x3=(x1 * f(x2) - x2 * f(x1))/(f(x2)-f(x1))
        print("{0}\t{1:.8f}\t{2:.8f}\t{3:.8f}\t{4:.8f}".format(count+1, x1, x2, x3, f(x3)))

        if f(x1) * f(x3) < 0:
            x2 = x3
        
        else:
            x1 = x3
        count += 1
    print("\nAfter {0} iterations, the root of the given equation is\n   x = {1}\nf(x) = {2}\n\n".format(count, x3, f(x3)))
    return True

funRF()
