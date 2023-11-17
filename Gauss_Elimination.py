import numpy


def gauss_elimination():
    n = int(input('Enter the number of variable: '))
    A = numpy.zeros((n,n+1))
    x = numpy.zeros(n)
    print('Enter the Coefficients of Augmented Matrix:')
    for i in range(n):
        for j in range(n+1):
            A[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
    print('The Augmented Matrix is:' )
    print(A)
    for i in range(n):
        if A[i][i] == 0.0:
            print('Divide by zero detected!')
            break
        for j in range(i+1, n):
            r = A[j][i]/A[i][i]
        
            for k in range(n+1):
                A[j][k] = A[j][k] - r * A[i][k]
                print(A)


    x[n-1] = A[n-1][n]/A[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = A[i][n]
    
        for j in range(i+1,n):
            x[i] = x[i] - A[i][j]*x[j]
    
        x[i] = x[i]/A[i][i]
    print('The upper triangular matrix is: ')
    print(A)

    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')

gauss_elimination()
