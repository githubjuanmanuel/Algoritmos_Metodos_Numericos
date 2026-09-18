# Calculadora de Métodos Numéricos en Python

Este proyecto implementa una **calculadora interactiva de métodos numéricos** desarrollada en Python.

El programa permite ingresar funciones matemáticas y aproximar raíces utilizando diferentes métodos estudiados en clase. Además, incluye un manual para escribir funciones correctamente, ejemplos de expresiones válidas y validaciones para evitar errores comunes durante la ejecución.

## 🎯 Objetivo

Aplicar mediante programación diferentes métodos numéricos para la aproximación de raíces de ecuaciones no lineales, permitiendo observar paso a paso las iteraciones realizadas por cada método.

El programa fue diseñado con fines académicos y como apoyo para practicar los procedimientos vistos en clase.

## 🧮 Métodos disponibles

Actualmente el programa incluye:

- Método de Bisección
- Método de Punto Fijo
- Método de Newton-Raphson

Cada método muestra las iteraciones realizadas hasta alcanzar la tolerancia definida por el usuario o hasta llegar al máximo de iteraciones permitido.

## 📌 Método de Bisección

El método de bisección aproxima una raíz dentro de un intervalo `[a, b]`.

Para poder utilizarlo, el programa verifica que:

```text
a < b
```

y que exista un cambio de signo:

```text
f(a) * f(b) < 0
```

Durante cada iteración se calcula el punto medio:

```text
P = (a + b) / 2
```

El programa muestra:

- Número de iteración.
- Extremo izquierdo `a`.
- Extremo derecho `b`.
- Punto medio `P`.
- Valor `f(P)`.
- Error aproximado.

## 📌 Método de Punto Fijo

Para utilizar Punto Fijo es necesario expresar la ecuación en la forma:

```text
x = g(x)
```

Por ejemplo, si se tiene:

```text
f(x) = x**3 + x - 1
```

una posible transformación es:

```text
g(x) = (1 - x)**(1/3)
```

El programa solicita un valor inicial `x0` y calcula sucesivamente:

```text
x_(n+1) = g(x_n)
```

El error utilizado es:

```text
|x_(n+1) - x_n|
```

El proceso termina cuando el error es menor que la tolerancia establecida.

## 📌 Método de Newton-Raphson

El método de Newton-Raphson utiliza la expresión:

```text
x_(n+1) = x_n - f(x_n) / f'(x_n)
```

Una de las principales características del programa es que la derivada de la función se calcula automáticamente utilizando **SymPy**.

Durante cada iteración se muestran:

- Número de iteración.
- Valor actual `x_n`.
- `f(x_n)`.
- `f'(x_n)`.
- Nuevo valor `x_(n+1)`.
- Error.

El programa también verifica que la derivada no sea cero o demasiado cercana a cero antes de realizar la división.

## 💻 Tecnologías utilizadas

- Python 3
- SymPy

SymPy se utiliza para:

- Interpretar expresiones matemáticas.
- Trabajar con funciones simbólicas.
- Calcular automáticamente derivadas.
- Convertir funciones simbólicas en funciones evaluables numéricamente.

## 📦 Instalación

Para ejecutar el programa se necesita tener instalado Python 3.

También se debe instalar la librería SymPy:

```bash
pip install sympy
```

Puedes verificar la instalación con:

```bash
python --version
```

y:

```bash
pip show sympy
```

## ▶️ Ejecución

Ejecuta el archivo desde la terminal:

```bash
python tarea_1.py
```

Dependiendo del sistema también puede utilizarse:

```bash
python3 tarea_1.py
```

Al iniciar aparecerá el menú principal:

```text
CALCULADORA DE MÉTODOS NUMÉRICOS

MÉTODOS DISPONIBLES

1. Método de Bisección
2. Método de Punto Fijo
3. Método de Newton-Raphson

AYUDA

4. Manual para ingresar funciones
5. Ejemplos de funciones

0. Salir
```

## ✍️ Cómo ingresar funciones

El programa utiliza la variable:

```text
x
```

### Operaciones básicas

```text
x**2
x**3
2*x + 5
1/x
(x + 1)/(x - 2)
```

Para multiplicar se debe utilizar:

```text
*
```

Ejemplo correcto:

```text
2*x
```

Para potencias se puede utilizar:

```text
**
```

Ejemplo:

```text
x**2
```

El programa también permite escribir `^` y lo transforma automáticamente en `**`.

## √ Raíces

Raíz cuadrada:

```text
sqrt(x)
```

Raíz cúbica:

```text
x**(1/3)
```

Ejemplo:

```text
sqrt(x) - 3
```

## 📐 Funciones trigonométricas

Se pueden utilizar:

```text
sin(x)
cos(x)
tan(x)
asin(x)
acos(x)
atan(x)
```

Ejemplo:

```text
cos(x) - x
```

Las funciones trigonométricas trabajan en **radianes**.

## 📈 Funciones exponenciales

Ejemplos:

```text
exp(x)
exp(-x) - x
2**x - 5
3**x - x**2
```

También puede utilizarse:

```text
E**x
```

## 📊 Logaritmos

### Logaritmo natural

```text
log(x)
```

También puede escribirse:

```text
ln(x)
```

El programa convierte automáticamente `ln(x)` en `log(x)`.

### Logaritmo base 10

```text
log(x, 10)
```

### Logaritmo base 2

```text
log(x, 2)
```

### Logaritmo en cualquier base

```text
log(x, base)
```

Por ejemplo:

```text
log(x, 3)
log(x, 5)
log(x, 7)
```

## 🔢 Constantes matemáticas

Número π:

```text
pi
```

Número e:

```text
E
```

Ejemplos:

```text
sin(pi*x)
x - pi
exp(x) - E
```

## 🧪 Ejemplos de funciones válidas

### Polinómicas

```text
x**2 - 4
x**3 - x - 2
x**2 - 5*x + 6
```

### Trigonométricas

```text
sin(x) - x/2
cos(x) - x
tan(x) - 2*x
```

### Exponenciales

```text
exp(x) - 3*x
exp(-x) - x
2**x - 5
```

### Logarítmicas

```text
log(x) - 1
log(x) + x - 2
log(x, 10) - 1
log(x, 2) - 3
```

### Funciones combinadas

```text
sin(x) + cos(x) - 1
exp(-x) + x - 1
log(x) + x**2 - 3
(x**3 + 2*x)/(x + 1)
```

## 🆘 Sistema de ayuda

Cuando el programa solicita una función, se puede escribir:

```text
ayuda
```

o:

```text
help
```

o simplemente:

```text
?
```

El programa mostrará nuevamente el manual de ingreso de funciones.

## ✅ Validaciones incluidas

El programa realiza diferentes verificaciones para evitar errores durante la ejecución.

Entre ellas se encuentran:

- Validación de funciones matemáticas.
- Validación de tolerancia mayor que cero.
- Validación del número máximo de iteraciones.
- Validación de valores numéricos.
- Comprobación de que `a < b` en Bisección.
- Comprobación del cambio de signo en Bisección.
- Control de errores de dominio.
- Detección de posibles divergencias en Punto Fijo.
- Verificación de derivadas cercanas a cero en Newton-Raphson.


## 📚 Propósito académico

Este programa fue desarrollado como ejercicio académico para comprender y aplicar métodos numéricos mediante programación.

Además de obtener una aproximación de la raíz, el objetivo es visualizar cada iteración y comprender cómo evoluciona el procedimiento hasta alcanzar la tolerancia establecida.

## 🚧 Estado del proyecto

Proyecto funcional y abierto a futuras mejoras.

Se pueden incorporar posteriormente otros métodos numéricos vistos en clase, nuevas validaciones, interfaces gráficas o generación de reportes de resultados.
