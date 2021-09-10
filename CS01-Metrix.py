import numpy as np
from numpy.matrixlib.defmatrix import matrix
Array = []]
Array2 = []
loop = 1
a = int(input("Enter Your loop:"))
b = int(input("Enter Your loop:"))

while( loop <= 2):
    print('enter your metrix',loop)
    for i in range(b) :
        for j in range(a) :
            print("MatrixColumns [",i,",",j,"] :",end =" ")
            if(loop == 1):
                MatrixOneInput = int(input(""))
                Array.append(MatrixOneInput)
            else:
                MatrixTwoInput = int(input(""))
                Array2.append(MatrixTwoInput)
    loop += 1
Newarray = np.asarray(Array)
Newarray2 = np.asarray(Array2)
NewarrayNumpy = Newarray.reshape(b,a)
NewarrayNumpy2 = Newarray2.reshape(b,a)
print(NewarrayNumpy,"\n==========")
print(NewarrayNumpy2,"\n==========")
sum = np.add(NewarrayNumpy,NewarrayNumpy2)
print(sum)