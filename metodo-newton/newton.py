import numpy as np;
import sys;



def MetodoGauss(A,b):
    n = len(b)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    Ab = np.append(A, b, axis=1)
    i =1 
    j = 1
    p = 0
    print(Ab)

if __name__ == "__main__":
    A = [[3,2,1,3,7], [1,1,2,9,2], [4,3,2,6,4], [2,5,7,12,8], [1,2,3,4,5]]
    b = [[1.87],[0.876],[2.56],[2,65],[4,765]]
    X = MetodoGauss(A, b)
print(A)