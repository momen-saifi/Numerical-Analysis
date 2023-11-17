import numpy


def gauss_seidel(A, b, x, mxit,ae):              
    for i in range(mxit):
        x_old = x.copy()
        for j in range(n):
            s1 = numpy.dot(A[j, :j], x[:j])
            s2 = numpy.dot(A[j, j + 1:], x_old[j + 1:])
            x[j] = (b[j] - s1 - s2) / A[j, j]
        if numpy.allclose(x, x_old, rtol=ae):
            return x
    return x



n = int(input("Enter no. of equations"))
A = numpy.zeros((n,n))
b = numpy.zeros(n)
print('Enter the Coefficients of Matrix:')
for i in range(n):
    for j in range(n):
        A[i][j] = float(input( 'A['+str(i)+']['+ str(j)+']='))
print('Enter Right-hand side vector :')
for i in range(n):
    b[i] = float(input( 'b['+str(i)+']='))
x = numpy.zeros(n)
print("Eneter the allowed error: ")
ae=float(input())
print("Eneter maximum number of iteration: ")
mxit=int(input())
                 
solution =  gauss_seidel(A, b, x,mxit,ae)
print("Solution:", solution)








