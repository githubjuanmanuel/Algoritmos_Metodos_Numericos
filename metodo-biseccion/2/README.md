# Método de Bisección en Python

Este proyecto implementa el **método de bisección** para aproximar la raíz de una función continua dentro de un intervalo dado.

En este caso se busca aproximar la raíz de la función:

```text
f(x) = ln(x) + x
```

utilizando el intervalo inicial:

```text
a = 0.5
b = 2.0
```

y una tolerancia de:

```text
tol = 0.01
```

---

## ¿Qué es el método de bisección?

El método de bisección es un método numérico utilizado para encontrar una aproximación de una raíz de una función.

Para aplicarlo, se parte de un intervalo `[a, b]` en el que la función cambia de signo. En cada iteración se calcula el punto medio:

```text
P = (a + b) / 2
```

Luego se evalúa la función en ese punto y se selecciona el nuevo intervalo que continúa conteniendo la raíz.

El proceso se repite hasta que el error o tolerancia sea suficientemente pequeño.

---

## Función utilizada

La función evaluada en este ejercicio es:

```python
def funcionBiseccion(x):
    return np.log(x) + x
```

Es decir:

```text
f(x) = ln(x) + x
```

La raíz de esta función se encuentra aproximadamente cerca de:

```text
x ≈ 0.567
```

---

## Cálculo de las iteraciones teóricas

El programa calcula una estimación del número de iteraciones necesarias mediante:

```python
def iteracionesBiseccion(a, b, tol):
    return np.log(2*(b-a)/tol) / np.log(2)
```

Esto permite comparar el número de iteraciones estimadas con las iteraciones realizadas por el algoritmo.

---

## Cálculo de la tolerancia

En cada iteración se calcula la tolerancia mediante:

```python
def toleranciaBiseccion(a, b):
    return 0.5 * (b-a)
```

El algoritmo termina cuando:

```python
TOL < tol
```

---

## Funcionamiento del algoritmo

El programa sigue los siguientes pasos:

1. Define el intervalo inicial `[a, b]`.
2. Evalúa la función en el extremo izquierdo.
3. Calcula el punto medio del intervalo.
4. Evalúa la función en el punto medio.
5. Calcula la tolerancia actual.
6. Comprueba si la tolerancia es menor que la tolerancia requerida.
7. Si todavía no se cumple el criterio de parada, selecciona el nuevo intervalo.
8. Repite el proceso hasta encontrar una aproximación aceptable o alcanzar el número máximo de iteraciones.

La actualización del intervalo se realiza mediante:

```python
if FP * FA < 0:
    b = P
else:
    a = P
    FA = FP
```

---

## Código

```python
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

while i <= No:
    P = (a+b)/2
    FP = funcionBiseccion(P)
    TOL = toleranciaBiseccion(a,b)

    print(
        f'Iteración: {i} | '
        f'a: {a} | '
        f'b: {b} | '
        f'P: {P} | '
        f'FP: {FP}'
    )

    if TOL < tol:
        print(
            f"Solución encontrada: "
            f"\nIteraciones teóricas: {i_teoricas} | "
            f"Iteración: {i} | "
            f"P: {P} | "
            f"FP: {FP}"
        )
        break

    if FP * FA < 0:
        b = P
    else:
        a = P
        FA = FP

    i = i + 1

if i > No:
    print("No encontró la solución")
```

---

## Requisitos

- Python 3
- NumPy

Para instalar NumPy:

```bash
pip install numpy
```

---

## Ejecución

Desde una terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python biseccion_2.py
```

El programa mostrará en consola los valores obtenidos en cada iteración:

```text
Iteración: 1 | a: ... | b: ... | P: ... | FP: ...
Iteración: 2 | a: ... | b: ... | P: ... | FP: ...
...
Solución encontrada
```

---

## Variables principales

| Variable | Descripción |
|---|---|
| `a` | Extremo izquierdo del intervalo |
| `b` | Extremo derecho del intervalo |
| `P` | Punto medio del intervalo |
| `FA` | Valor de la función en `a` |
| `FP` | Valor de la función en `P` |
| `tol` | Tolerancia requerida |
| `TOL` | Tolerancia calculada en cada iteración |
| `No` | Número máximo de iteraciones |
| `i` | Contador de iteraciones |
| `i_teoricas` | Número estimado de iteraciones |

---

## Objetivo académico

Este ejercicio permite comprender la aplicación práctica del método de bisección y conceptos relacionados con métodos numéricos, entre ellos:

- búsqueda de raíces;
- intervalos;
- cambio de signo;
- aproximaciones sucesivas;
- tolerancia y error;
- estructuras repetitivas;
- estructuras condicionales.

---

## Autor

Proyecto desarrollado por Juan Manuel Montoya Montoya como actividad académica.
