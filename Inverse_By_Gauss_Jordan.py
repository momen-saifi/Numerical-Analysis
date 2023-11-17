import numpy


def gauss_jordan():
    n = int(input('Enter the order of marrix: '))
    A = numpy.zeros((n,2*n))
   
    print('Enter the Coefficients of Augmented Matrix:')
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j+n] = 1
    print('The Augmented Matrix is:')
    print(A)                
    for i in range(n):
        if A[i][i] == 0.0:
            print('Divide by zero detected!')
            break
        for j in range(n):
            if i!=j:
                r = A[j][i]/A[i][i]
        
                for k in range(2*n):
                    A[j][k] = A[j][k] - r * A[i][k]
    for i in range(n):
        divisor = A[i][i]
        for j in range(2*n):
            A[i][j]=A[i][j]/divisor
            
   

    print("The Inverse matrix is: ")

    for i in range(n):
        for j in range(n ,2*n):
            print(A[i][j], end='\t')
        print()

gauss_jordan()
