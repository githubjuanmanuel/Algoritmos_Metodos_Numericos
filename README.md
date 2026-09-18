# Algoritmos de Métodos Numéricos en JavaScript y Python

Este repositorio reúne diferentes algoritmos desarrollados en **JavaScript** y **Python** a partir de los temas, métodos y ejercicios vistos en clase.

La idea principal es utilizar este espacio como una recopilación organizada de los algoritmos implementados durante el curso, permitiendo consultar su funcionamiento, comparar métodos y documentar el proceso de aprendizaje en ambos lenguajes de programación.

## 🎯 Objetivo

Implementar y documentar algoritmos relacionados con los temas estudiados en clase, especialmente aquellos que puedan resolverse mediante programación y que permitan reforzar conceptos matemáticos, lógicos y computacionales.

Cada algoritmo incluido en este repositorio busca mostrar:

* El problema o método que se desea resolver.
* La lógica utilizada para desarrollar la solución.
* La implementación en JavaScript y/o Python.
* Los valores de entrada utilizados.
* Los resultados obtenidos.
* Una breve explicación del funcionamiento.

## 💻 Tecnologías utilizadas

Los ejercicios pueden estar desarrollados con:

* JavaScript
* Node.js
* Python
* NumPy, cuando el ejercicio en Python lo requiera.

El objetivo es practicar los mismos conceptos utilizando diferentes lenguajes y observar las similitudes y diferencias entre sus implementaciones.

## 📂 Organización del repositorio

Cada tema puede almacenarse dentro de su propia carpeta, incluyendo las implementaciones disponibles en JavaScript y Python y, cuando sea necesario, un README específico con la explicación del algoritmo.

Ejemplo de estructura:

```text
Algoritmos_Metodos_Numericos/
│
├── metodo-biseccion/
│   ├── biseccion.js
│   ├── biseccion.py
│   └── README.md
│
├── metodo-newton-raphson/
│   ├── newtonRaphson.js
│   ├── newton_raphson.py
│   └── README.md
│
├── metodo-secante/
│   ├── secante.js
│   ├── secante.py
│   └── README.md
│
└── README.md
```

No necesariamente todos los algoritmos tendrán desde el inicio una implementación en ambos lenguajes. La estructura puede ampliarse a medida que se estudien nuevos temas y se desarrollen nuevas versiones.

## 📚 Algoritmos incluidos

### Método de Bisección

Método numérico utilizado para aproximar una raíz de una función continua dentro de un intervalo en el que existe un cambio de signo.

La implementación permite observar cada iteración, el punto medio del intervalo y el error aproximado hasta alcanzar una tolerancia determinada.

Este método puede encontrarse implementado tanto en **JavaScript** como en **Python**, permitiendo comparar la lógica utilizada en ambos lenguajes.

A medida que avance el curso se agregarán nuevos algoritmos desarrollados a partir de los ejercicios y métodos vistos en clase.

## ▶️ Ejecución de los algoritmos

Dependiendo del lenguaje utilizado, el procedimiento de ejecución cambia.

### JavaScript

Para ejecutar los programas desarrollados en JavaScript es necesario tener instalado **Node.js**.

Después de clonar el repositorio:

```bash
git clone https://github.com/githubjuanmanuel/Algoritmos_Metodos_Numericos.git
```

Ingresa a la carpeta correspondiente al algoritmo:

```bash
cd metodo-biseccion
```

Ejecuta el archivo JavaScript:

```bash
node biseccion.js
```

### Python

Para ejecutar los programas desarrollados en Python es necesario tener instalado **Python 3**.

Dentro de la carpeta correspondiente al algoritmo, ejecuta:

```bash
python biseccion.py
```

Dependiendo de la configuración del sistema también puede ser necesario utilizar:

```bash
python3 biseccion.py
```

Algunos ejercicios pueden requerir librerías adicionales como **NumPy**. En ese caso se pueden instalar mediante:

```bash
pip install numpy
```

Los nombres de los archivos pueden cambiar dependiendo del algoritmo desarrollado.

## 🧠 Metodología de trabajo

Para cada nuevo tema visto en clase se puede seguir el siguiente proceso:

1. Analizar el problema o método matemático.
2. Identificar los datos de entrada.
3. Definir las fórmulas y condiciones necesarias.
4. Diseñar el algoritmo.
5. Implementarlo en JavaScript y/o Python.
6. Ejecutar diferentes pruebas.
7. Comparar los resultados obtenidos.
8. Revisar el comportamiento de las implementaciones.
9. Documentar el ejercicio dentro del repositorio.

Cuando un mismo algoritmo sea desarrollado en ambos lenguajes, se busca que las implementaciones mantengan una lógica equivalente para facilitar su comparación.

## 📈 Propósito del repositorio

Este repositorio tiene un propósito principalmente académico y busca servir como evidencia del proceso de aprendizaje y práctica de los algoritmos desarrollados durante el curso.

También puede utilizarse como material de consulta para:

* Repasar los métodos numéricos estudiados.
* Consultar implementaciones anteriores.
* Comparar soluciones desarrolladas en JavaScript y Python.
* Reforzar conceptos de programación.
* Observar la evolución de los algoritmos realizados durante las clases.

## 🚧 Estado del proyecto

Repositorio en desarrollo.

Se agregarán nuevos algoritmos y nuevas implementaciones en **JavaScript** y **Python** a medida que se estudien nuevos temas y ejercicios en clase.
