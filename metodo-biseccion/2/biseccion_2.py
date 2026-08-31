import numpy as np

def funcionBiseccion(x):
    return np.log(x) + x


def iteracionesBiseccion(a, b, tol):
    return np.log(2*(b-a)/tol) / np.log(2)

def toleranciaBiseccion(a,b):
    return 0.5*(b-a)


a = 0.5
b = 2.0
FA = funcionBiseccion(a)
tol = 0.01
No = 100
i = 1
i_teoricas = round(iteracionesBiseccion(a,b,tol))

while (i <= No):
    P = (a+b)/2
    FP = funcionBiseccion(P)
    TOL = toleranciaBiseccion(a,b)
    print(f'Iteración: {i} | a: {a} | b: {b} | P: {P} | FP: {FP} \n')

    if(TOL<tol):
        print(f"Solución encontrada: \n Iteraciones teóricas: {i_teoricas} | Iteración: {i} | P: {P} | FP: {FP}")
        break

    if((FP*FA) < 0):
        b = P
    else:
        a = P
        FA = FP
    
    i=i+1

if (i > No):
    print("No encontro la solución")
