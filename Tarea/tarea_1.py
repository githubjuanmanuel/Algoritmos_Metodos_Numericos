import sympy as sp


# ============================================================
# CONFIGURACIÓN DE LA VARIABLE
# ============================================================

x = sp.symbols("x")


# ============================================================
# MANUAL PARA INGRESAR FUNCIONES
# ============================================================

def mostrar_manual_funciones():
    print("\n" + "=" * 75)
    print("              MANUAL PARA INGRESAR FUNCIONES")
    print("=" * 75)

    print("""
Escriba la función usando la variable x.

-----------------------------------------------------------
1. OPERACIONES BÁSICAS
-----------------------------------------------------------

Operación                         Forma de escribirla
-----------------------------------------------------------
x al cuadrado                     x**2
x al cubo                         x**3
x elevado a n                     x**n
2x + 5                            2*x + 5
1 dividido por x                  1/x
(x + 1) dividido por (x - 2)      (x + 1)/(x - 2)

IMPORTANTE:

Para multiplicar utilice *

Correcto:
2*x

Incorrecto:
2x


Para elevar utilice **

Correcto:
x**2

Incorrecto:
x^2


-----------------------------------------------------------
2. RAÍCES
-----------------------------------------------------------

Raíz cuadrada de x:

sqrt(x)

Ejemplo:

sqrt(x) - 3


Raíz cúbica:

x**(1/3)

Ejemplo:

x**(1/3) - 2


Raíz cuarta:

x**(1/4)


Raíz n-ésima:

x**(1/n)


-----------------------------------------------------------
3. FUNCIONES TRIGONOMÉTRICAS
-----------------------------------------------------------

Seno:

sin(x)

Coseno:

cos(x)

Tangente:

tan(x)


También están disponibles:

asin(x)      -> arco seno
acos(x)      -> arco coseno
atan(x)      -> arco tangente


Ejemplos:

sin(x) - x/2

cos(x) - x

tan(x) - 2*x


IMPORTANTE:

Las funciones trigonométricas trabajan en RADIANES.


-----------------------------------------------------------
4. FUNCIONES EXPONENCIALES
-----------------------------------------------------------

e elevado a x:

exp(x)

También puede escribir:

E**x


Ejemplos:

exp(x) - 3*x

exp(-x) - x

2**x - 5

3**x - x**2


-----------------------------------------------------------
5. LOGARITMOS
-----------------------------------------------------------

LOGARITMO NATURAL
Base e:

log(x)

Ejemplo:

log(x) - 1


También puede escribirse como:

ln(x)

El programa convertirá ln(x) automáticamente en log(x).


-----------------------------------------------------------

LOGARITMO BASE 10:

log(x, 10)

Ejemplo:

log(x, 10) - 2

Esto representa:

log₁₀(x)


-----------------------------------------------------------

LOGARITMO BASE 2:

log(x, 2)

Ejemplo:

log(x, 2) - 3

Esto representa:

log₂(x)


-----------------------------------------------------------

LOGARITMO EN CUALQUIER BASE:

log(x, base)

Ejemplos:

log(x, 3)

log(x, 5)

log(x, 7)

log(x, 10)


Ejemplo de ecuación:

log(x, 2) - 4

Su solución sería aproximadamente:

x = 16


-----------------------------------------------------------
6. CONSTANTES MATEMÁTICAS
-----------------------------------------------------------

Número pi:

pi


Número e:

E


Ejemplos:

sin(pi*x)

x - pi

exp(x) - E


-----------------------------------------------------------
7. FUNCIONES COMBINADAS
-----------------------------------------------------------

Puede combinar varias operaciones.

Ejemplos:

x**3 - x - 2

sqrt(x) + x - 5

sin(x) + cos(x) - 1

exp(-x) - x

log(x) + x - 2

log(x, 10) + x - 3

log(x, 2) - x/2

(x**3 + 2*x)/(x + 1)


-----------------------------------------------------------
8. EJEMPLOS COMPLETOS
-----------------------------------------------------------

Polinómica:

x**3 - x - 2


Cuadrática:

x**2 - 5*x + 6


Trigonométrica:

cos(x) - x


Exponencial:

exp(-x) - x


Logaritmo natural:

log(x) + x - 2


Logaritmo base 10:

log(x, 10) - 1


Logaritmo base 2:

log(x, 2) - 3


Raíz cuadrada:

sqrt(x) - 3


Combinada:

sin(x) + log(x) - 1


-----------------------------------------------------------
9. AYUDA RÁPIDA
-----------------------------------------------------------

Mientras el programa solicita una función puede escribir:

ayuda

help

?

para volver a mostrar este manual.

""")

    print("=" * 75)


# ============================================================
# EJEMPLOS DE FUNCIONES
# ============================================================

def mostrar_ejemplos():
    print("\n" + "=" * 70)
    print("                  EJEMPLOS DE FUNCIONES")
    print("=" * 70)

    print("""
1. POLINÓMICAS

   x**2 - 4

   x**3 - x - 2

   x**2 - 5*x + 6

   x**4 - 3*x**2 + 1


2. TRIGONOMÉTRICAS

   sin(x) - x/2

   cos(x) - x

   tan(x) - 2*x


3. EXPONENCIALES

   exp(x) - 3*x

   exp(-x) - x

   2**x - 5


4. LOGARITMOS

   log(x) - 1

   log(x) + x - 2

   log(x, 10) - 1

   log(x, 2) - 3

   log(x, 5) - 2


5. RAÍCES

   sqrt(x) - 2

   sqrt(x + 4) - 3

   x**(1/3) - 2


6. FUNCIONES COMBINADAS

   sin(x) + cos(x) - 1

   exp(-x) + x - 1

   log(x) + x**2 - 3

   log(x, 10) + x - 2

   (x**3 + 2*x)/(x + 1)

""")

    print("=" * 70)


# ============================================================
# MENÚ PARA INGRESAR FUNCIONES
# ============================================================

def menu_funcion():

    while True:

        print("\n" + "=" * 60)
        print("              INGRESO DE LA FUNCIÓN")
        print("=" * 60)

        print("""
1. Ingresar función
2. Ver manual para escribir funciones
3. Ver ejemplos de funciones
""")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            return

        elif opcion == "2":
            mostrar_manual_funciones()

        elif opcion == "3":
            mostrar_ejemplos()

        else:
            print("\nOpción no válida. Intente nuevamente.")


# ============================================================
# FUNCIÓN PARA NORMALIZAR EXPRESIONES
# ============================================================

def normalizar_expresion(expresion):

    expresion = expresion.strip()

    # Permitir escribir ln(x)
    expresion = expresion.replace("ln(", "log(")

    # Permitir usar ^ de manera intuitiva
    expresion = expresion.replace("^", "**")

    return expresion


# ============================================================
# FUNCIÓN PARA LEER EXPRESIONES MATEMÁTICAS
# ============================================================

def leer_funcion(mensaje):

    while True:

        try:

            expresion = input(mensaje).strip()

            if expresion.lower() in ["ayuda", "help", "?"]:
                mostrar_manual_funciones()
                continue

            expresion = normalizar_expresion(expresion)

            funcion_simbolica = sp.sympify(expresion)

            funcion = sp.lambdify(
                x,
                funcion_simbolica,
                modules=["math"]
            )

            return funcion_simbolica, funcion

        except Exception as error:

            print("\nLa función ingresada no es válida.")

            print("""
Ejemplos válidos:

x**3 - x - 2

x^2 - 4

sin(x) - x

sqrt(x) - 3

log(x) - 1

log(x, 10) - 2

log(x, 2) - 3

Recuerde:

Multiplicación:
2*x

Potencia:
x**2

Raíz:
sqrt(x)

Logaritmo natural:
log(x)

Logaritmo base 10:
log(x, 10)

Logaritmo base 2:
log(x, 2)

Escriba 'ayuda' para consultar el manual.
""")


# ============================================================
# MÉTODO DE BISECCIÓN
# ============================================================

def biseccion(funcion, a, b, tolerancia, max_iteraciones):

    print("\n" + "=" * 95)
    print("                         MÉTODO DE BISECCIÓN")
    print("=" * 95)

    try:

        fa = funcion(a)
        fb = funcion(b)

    except Exception:
        print("\nNo fue posible evaluar la función en el intervalo.")
        return None

    if fa * fb > 0:

        print("\nEl método de bisección no puede comenzar.")
        print("f(a) y f(b) tienen el mismo signo.")

        print(f"\nf(a) = {fa}")
        print(f"f(b) = {fb}")

        print("\nDebe escoger un intervalo donde:")
        print("f(a) * f(b) < 0")

        return None

    print(
        f"\n{'Iter':<8}"
        f"{'a':<16}"
        f"{'b':<16}"
        f"{'P':<16}"
        f"{'f(P)':<18}"
        f"{'Error':<16}"
    )

    print("-" * 95)

    P_anterior = None

    for iteracion in range(1, max_iteraciones + 1):

        P = (a + b) / 2

        try:
            fP = funcion(P)

        except Exception:
            print("\nError al evaluar la función.")
            return None

        if P_anterior is None:

            error = float("inf")
            error_texto = "---"

        else:

            error = abs((b - a)/2)
            error_texto = f"{error:.10f}"

        print(
            f"{iteracion:<8}"
            f"{a:<16.10f}"
            f"{b:<16.10f}"
            f"{P:<16.10f}"
            f"{fP:<18.10f}"
            f"{error_texto:<16}"
        )

        # Condiciones de parada

        if P_anterior is not None and error < tolerancia:

            print("\nConvergencia alcanzada porque el error es menor")
            print("que la tolerancia.")

            print(f"\nRaíz aproximada: {P:.12f}")
            print(f"f(raíz): {fP:.12f}")
            print(f"Iteraciones: {iteracion}")

            return P

        # Actualizar intervalo

        if fa * fP < 0:

            b = P

        else:

            a = P
            fa = fP
        P_anterior = P

    print("\nSe alcanzó el número máximo de iteraciones.")

    print(f"Última aproximación: {P:.12f}")

    return P


# ============================================================
# MÉTODO DE PUNTO FIJO
# ============================================================

def punto_fijo(g, x0, tolerancia, max_iteraciones):

    print("\n" + "=" * 85)
    print("                         MÉTODO DE PUNTO FIJO")
    print("=" * 85)

    print(
        f"\n{'Iter':<10}"
        f"{'x_n':<22}"
        f"{'x_(n+1)':<22}"
        f"{'Error absoluto':<22}"
    )

    print("-" * 85)

    for iteracion in range(1, max_iteraciones + 1):

        try:

            x1 = g(x0)

        except Exception:

            print("\nError al evaluar g(x).")
            print("Revise el dominio de la función.")

            return None

        error = abs(x1 - x0)

        print(
            f"{iteracion:<10}"
            f"{x0:<22.12f}"
            f"{x1:<22.12f}"
            f"{error:<22.12f}"
        )

        if error < tolerancia:

            print("\nConvergencia alcanzada.")

            print(f"\nRaíz aproximada: {x1:.12f}")
            print(f"Iteraciones: {iteracion}")

            return x1

        # Protección ante divergencia

        if abs(x1) > 1e100:

            print("\nEl método parece estar divergiendo.")

            return None

        x0 = x1

    print("\nSe alcanzó el número máximo de iteraciones.")

    print(f"Última aproximación: {x1:.12f}")

    return x1


# ============================================================
# MÉTODO DE NEWTON-RAPHSON
# ============================================================

def newton(funcion_simbolica, funcion, x0, tolerancia, max_iteraciones):

    derivada_simbolica = sp.diff(funcion_simbolica, x)

    derivada = sp.lambdify(
        x,
        derivada_simbolica,
        modules=["math"]
    )

    print("\n" + "=" * 115)
    print("                          MÉTODO DE NEWTON-RAPHSON")
    print("=" * 115)

    print(f"\nf(x)  = {funcion_simbolica}")
    print(f"f'(x) = {derivada_simbolica}")

    print(
        f"\n{'Iter':<8}"
        f"{'x_n':<22}"
        f"{'f(x_n)':<22}"
        f'{"f\'(x_n)":<22}'
        f"{'x_(n+1)':<22}"
        f"{'Error':<18}"
    )

    print("-" * 115)

    for iteracion in range(1, max_iteraciones + 1):

        try:

            fx = funcion(x0)
            dfx = derivada(x0)

        except Exception:

            print("\nError al evaluar la función o su derivada.")
            print("Revise el dominio de la función.")

            return None

        # Evitar división entre cero

        if abs(dfx) < 1e-15:

            print("\nNewton-Raphson no puede continuar.")

            print("La derivada es cero o demasiado cercana a cero.")

            print(f"\nx = {x0}")
            print(f"f'(x) = {dfx}")

            return None

        x1 = x0 - (fx / dfx)

        error = abs(x1 - x0)

        print(
            f"{iteracion:<8}"
            f"{x0:<22.12f}"
            f"{fx:<22.12f}"
            f"{dfx:<22.12f}"
            f"{x1:<22.12f}"
            f"{error:<18.12f}"
        )

        if error < tolerancia :

            print("\nConvergencia alcanzada.")

            print(f"\nRaíz aproximada: {x1:.12f}")
            print(f"Iteraciones: {iteracion}")

            return x1

        x0 = x1

    print("\nSe alcanzó el número máximo de iteraciones.")

    print(f"Última aproximación: {x1:.12f}")

    return x1


# ============================================================
# LEER TOLERANCIA
# ============================================================

def leer_tolerancia():

    while True:

        try:

            tolerancia = float(
                input(
                    "\nIngrese la tolerancia "
                    "[ejemplo: 0.000001]: "
                )
            )

            if tolerancia <= 0:
                print("La tolerancia debe ser mayor que cero.")
                continue

            return tolerancia

        except ValueError:

            print("Debe ingresar un número válido.")


# ============================================================
# LEER MÁXIMO DE ITERACIONES
# ============================================================

def leer_max_iteraciones():

    while True:

        try:

            max_iteraciones = int(
                input(
                    "Ingrese el máximo de iteraciones "
                    "[ejemplo: 100]: "
                )
            )

            if max_iteraciones <= 0:
                print(
                    "El número de iteraciones debe ser mayor que cero."
                )
                continue

            return max_iteraciones

        except ValueError:

            print("Debe ingresar un número entero.")


# ============================================================
# EJECUTAR BISECCIÓN
# ============================================================

def ejecutar_biseccion():

    print("\n" + "=" * 60)
    print("                   BISECCIÓN")
    print("=" * 60)

    menu_funcion()

    funcion_simbolica, funcion = leer_funcion(
        "\nIngrese f(x): "
    )

    print(f"\nFunción ingresada:")
    print(f"f(x) = {funcion_simbolica}")

    tolerancia = leer_tolerancia()
    max_iteraciones = leer_max_iteraciones()

    while True:

        try:

            a = float(
                input("\nIngrese el extremo izquierdo a: ")
            )

            b = float(
                input("Ingrese el extremo derecho b: ")
            )

            if a >= b:

                print(
                    "\nEl extremo a debe ser menor que b."
                )

                continue

            break

        except ValueError:

            print("Debe ingresar valores numéricos.")

    biseccion(
        funcion,
        a,
        b,
        tolerancia,
        max_iteraciones
    )


# ============================================================
# EJECUTAR PUNTO FIJO
# ============================================================

def ejecutar_punto_fijo():

    print("\n" + "=" * 60)
    print("                   PUNTO FIJO")
    print("=" * 60)

    menu_funcion()

    funcion_simbolica, funcion = leer_funcion(
        "\nIngrese la ecuación original f(x): "
    )

    print(f"\nEcuación ingresada:")
    print(f"f(x) = {funcion_simbolica}")

    print("\nPara aplicar Punto Fijo se necesita escribir:")
    print()
    print("              x = g(x)")
    print()

    print("Por ejemplo, si:")
    print()
    print("f(x) = x**3 + x - 1")
    print()
    print("una posible transformación es:")
    print()
    print("g(x) = (1 - x)**(1/3)")
    print()

    print(
        "Puede escribir 'ayuda' si necesita consultar "
        "el manual."
    )

    g_simbolica, g = leer_funcion(
        "\nIngrese g(x): "
    )

    print(f"\ng(x) = {g_simbolica}")

    tolerancia = leer_tolerancia()
    max_iteraciones = leer_max_iteraciones()

    while True:

        try:

            x0 = float(
                input("\nIngrese el valor inicial x0: ")
            )

            break

        except ValueError:

            print("x0 debe ser un número.")

    punto_fijo(
        g,
        x0,
        tolerancia,
        max_iteraciones
    )


# ============================================================
# EJECUTAR NEWTON-RAPHSON
# ============================================================

def ejecutar_newton():

    print("\n" + "=" * 60)
    print("                NEWTON-RAPHSON")
    print("=" * 60)

    menu_funcion()

    funcion_simbolica, funcion = leer_funcion(
        "\nIngrese f(x): "
    )

    print(f"\nFunción ingresada:")
    print(f"f(x) = {funcion_simbolica}")

    tolerancia = leer_tolerancia()
    max_iteraciones = leer_max_iteraciones()

    while True:

        try:

            x0 = float(
                input("\nIngrese el valor inicial x0: ")
            )

            break

        except ValueError:

            print("x0 debe ser un número.")

    newton(
        funcion_simbolica,
        funcion,
        x0,
        tolerancia,
        max_iteraciones
    )


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("            CALCULADORA DE MÉTODOS NUMÉRICOS")
        print("=" * 65)

        print("""
MÉTODOS DISPONIBLES

1. Método de Bisección
2. Método de Punto Fijo
3. Método de Newton-Raphson

AYUDA

4. Manual para ingresar funciones
5. Ejemplos de funciones

0. Salir
""")

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        # ----------------------------------------------------
        # BISECCIÓN
        # ----------------------------------------------------

        if opcion == "1":

            ejecutar_biseccion()

        # ----------------------------------------------------
        # PUNTO FIJO
        # ----------------------------------------------------

        elif opcion == "2":

            ejecutar_punto_fijo()

        # ----------------------------------------------------
        # NEWTON-RAPHSON
        # ----------------------------------------------------

        elif opcion == "3":

            ejecutar_newton()

        # ----------------------------------------------------
        # MANUAL
        # ----------------------------------------------------

        elif opcion == "4":

            mostrar_manual_funciones()

        # ----------------------------------------------------
        # EJEMPLOS
        # ----------------------------------------------------

        elif opcion == "5":

            mostrar_ejemplos()

        # ----------------------------------------------------
        # SALIR
        # ----------------------------------------------------

        elif opcion == "0":

            print("\n" + "=" * 65)
            print("Programa finalizado.")
            print("=" * 65)

            break

        else:

            print(
                "\nOpción no válida. "
                "Seleccione una opción del menú."
            )


# ============================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()