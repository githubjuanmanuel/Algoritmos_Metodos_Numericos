# Método de Bisección en JavaScript

Este proyecto implementa el **método de bisección** utilizando JavaScript para aproximar la raíz de una función dentro de un intervalo dado.

## 📌 Descripción

El método de bisección es un método numérico utilizado para encontrar aproximadamente una raíz de una función continua.

El algoritmo divide repetidamente un intervalo `[a, b]` en dos partes y selecciona el subintervalo en el cual se encuentra la raíz, hasta alcanzar la tolerancia establecida.

En este ejercicio se trabaja con la función:

```text
f(x) = ln(x) + x
```

donde `ln(x)` corresponde al logaritmo natural.

## 🧮 Fórmula utilizada

En cada iteración se calcula el punto medio del intervalo:

```text
P = (a + b) / 2
```

También se evalúa el error aproximado mediante:

```text
(b - a) / 2
```

El proceso termina cuando este valor es menor que la tolerancia establecida.

## 💻 Tecnologías utilizadas

- JavaScript
- Node.js

## 📂 Estructura del proyecto

```text
.
├── biseccion.js
└── README.md
```

## ⚙️ Funcionamiento del programa

El archivo `biseccion.js` contiene tres funciones principales:

### `metodoBiseccion(a, b, Tol)`

Ejecuta el método de bisección utilizando:

- `a`: límite inferior del intervalo.
- `b`: límite superior del intervalo.
- `Tol`: tolerancia permitida.

Durante cada iteración se calcula el punto medio y se determina si el intervalo debe reducirse por la izquierda o por la derecha.

### `calcularIteraciones(a, b, Tol)`

Calcula una estimación del número de iteraciones necesarias para alcanzar la tolerancia especificada.

### `imprimir(...)`

Muestra en consola los datos correspondientes a cada iteración:

- Número de iteración.
- Valor de `a`.
- Valor de `b`.
- Punto medio `P`.
- Evaluaciones de la función.
- Error aproximado.
- Comparación del error con la tolerancia.

## ▶️ Ejecución

Para ejecutar el proyecto se necesita tener instalado **Node.js**.

Primero, clona el repositorio:

```bash
git clone https://github.com/githubjuanmanuel/Algoritmos_Metodos_Numericos.git
```

Ingresa a la carpeta del proyecto:

```bash
cd metodo-biseccion
```

Ejecuta el programa:

```bash
node biseccion.js
```

## 🧪 Ejemplo utilizado

El programa se ejecuta con los siguientes valores:

```javascript
metodoBiseccion(0.5, 2, 0.01);
```

Por lo tanto:

```text
a = 0.5
b = 2
Tolerancia = 0.01
```

El algoritmo realiza las iteraciones necesarias hasta que el error aproximado sea menor que `0.01` o hasta alcanzar el máximo de iteraciones establecido.

## 📊 Salida

En cada iteración el programa muestra información similar a:

```text
Iteración: 1
| i: 1 | a: ... | b: ... | P: ... | FA: ... | FP: ... | error < tolerancia = ... |
```

Al finalizar también muestra el número aproximado de iteraciones calculadas y la cantidad de iteraciones ejecutadas.

## 🎯 Objetivo académico

Este proyecto fue desarrollado como ejercicio académico para aplicar el **método numérico de bisección** mediante programación en JavaScript, permitiendo observar paso a paso cómo se reduce el intervalo hasta obtener una aproximación de la raíz.

## 👨‍💻 Autor

Proyecto desarrollado por Juan Manuel Montoya Montoya como actividad académica.
