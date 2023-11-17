from sympy import symbols, lambdify, diff
import math



    
def function():
    
    x = symbols('x')
    equation = str(input("Enter the function in the form \'x**3 + 4*x**2 - 10\': "))
    f = lambdify(x, equation)
    df = lambdify(x, diff(equation))
    
    a = int(input("If you want to enter initial guess press 1 outherwise press 2 "))


    if(a==2):
        
        
        
        x1=0.0
        x2=0.0
        for i in range(-10,10):
            
            r1=i
            r2=i+1
            if(f(r1)*f(r2)<0):
                x1=r1
                x2=r2
                x0=(x1+x2)/2
            
         
            
            
            
            
    if (a==1):
        
   
        while True:
            
            x0 = float(input("Enter the guess value: "))
            if (df(x0)!=0):
                print("Root lies for this initial guess")
                break
            else:
                print("Root does not exist  (Diverge),  Please choose another guess.")
               

    pos = float(input("Enter the desired Precision in the form of\'0.00001\': "))
    Iteration = int(input("Enter maximum number of iterations: "))
    

    count = 0
    x1 = 0.0
   
   

    print("\nIterations\tx0\t\tx1\t\tf(x1)")
    while (abs(f(x1))>=pos or count<Iteration) :
        x1 = x0 - (f(x0) / df(x0))
        
        print("{0}\t{1:.8f}\t{2:.8f}\t{3:.8f}".format(count+1, x0, x1, f(x1)))

        x0 = x1
        count += 1
    print("\nAfter {0} iterations, the root of the given equation is\n   x = {1}\nf(x) = {2}\n\n".format(count, x1, f(x1)))
  
    return True
function()
