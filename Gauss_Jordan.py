import numpy


def gauss_jordan():
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
        for j in range(n):
            if i!=j:
                r = A[j][i]/A[i][i]
        
                for k in range(n+1):
                    A[j][k] = A[j][k] - r * A[i][k]
   

    print('The diagonal matrix is: ')
    print(A)

    print('\nRequired solution is: ')
    for i in range(n):
                x[i] = A[i][n]/A[i][i]

                print('X%d = %0.2f' %(i,x[i]), end = '\t')

gauss_jordan()
