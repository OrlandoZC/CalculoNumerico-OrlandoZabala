# ==========================================================
# MÉTODO DE BISECCIÓN
# Autor: Orlando Zabala 
# C.I: 31.256.875
# Materia: Cálculo Numérico
# Descripción:
# Implementación del método de bisección para el cálculo
# numérico de raíces de ecuaciones no lineales.
# ==========================================================

import sympy as sp


def biseccion(f_str, a, b, tol=1e-5, max_iter=100):
    """
    Método de Bisección para aproximar raíces de una función.

    Parámetros:
    f_str     : función en formato texto (ej: 'x**3 - x - 2')
    a         : extremo inferior del intervalo
    b         : extremo superior del intervalo
    tol       : tolerancia del error
    max_iter  : máximo número de iteraciones

    Retorna:
    Aproximación de la raíz o None si falla.
    """

    # ------------------------------------------------------
    # 1) Definir variable simbólica
    # ------------------------------------------------------
    x = sp.symbols('x')

    # ------------------------------------------------------
    # 2) Convertir texto a expresión simbólica
    # ------------------------------------------------------
    try:
        f_expr = sp.sympify(f_str)
    except:
        print(" Error: La función no pudo interpretarse correctamente.")
        return None

    # Convertir expresión simbólica en función numérica
    f = sp.lambdify(x, f_expr, "math")

    # ------------------------------------------------------
    # 3) Verificación del Teorema de Bolzano
    # ------------------------------------------------------
    try:
        fa = f(a)
        fb = f(b)
    except:
        print(" Error al evaluar la función en los extremos.")
        return None

    if fa * fb >= 0:
        print(" No existe cambio de signo en el intervalo.")
        print("El método requiere que f(a)*f(b) < 0.")
        return None

    # ------------------------------------------------------
    # 4) Tabla de iteraciones
    # ------------------------------------------------------
    print("\nTabla de Iteraciones:")
    print(f"{'Iter':<5}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<14}{'Error abs':<14}{'Error teórico':<14}")
    print("-" * 85)

    c_anterior = None

    for i in range(1, max_iter + 1):

        # Punto medio
        c = (a + b) / 2
        fc = f(c)

        # Error absoluto entre aproximaciones
        if c_anterior is None:
            error_abs = 0
        else:
            error_abs = abs(c - c_anterior)

        # Error teórico (cota máxima garantizada)
        error_teorico = abs(b - a) / 2

        print(f"{i:<5}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fc:<14.6f}{error_abs:<14.6f}{error_teorico:<14.6f}")

        # Condición de parada
        if abs(fc) < tol or error_teorico < tol:
            print("\nConvergencia alcanzada.")
            return c

        # Actualización del intervalo
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c_anterior = c

    print("\nSe alcanzó el número máximo de iteraciones.")
    return (a + b) / 2


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

while True:

    print("\n" + "=" * 65)
    print("        CALCULADORA - MÉTODO DE BISECCIÓN")
    print("=" * 65)

    # ------------------ GUÍA PARA EL USUARIO ------------------

    print("\nGUÍA PARA ESCRIBIR LA FUNCIÓN:")
    print("• Use la variable x.")
    print("• Potencias: x**2 , x**3")
    print("• Raíz cuadrada: sqrt(x)")
    print("• Funciones trigonométricas: sin(x), cos(x), tan(x)")
    print("• Exponencial: exp(x)")
    print("• Logaritmo natural: log(x)")
    print("\nEjemplos válidos:")
    print("   x**3 - x - 2")
    print("   cos(x) - x")
    print("   exp(x) - 3*x")
    print("-" * 65)

    f_usuario = input("Ingrese f(x): ")

    try:
        a = float(input("Límite inferior (a): "))
        b = float(input("Límite superior (b): "))

        tol_input = input("Tolerancia (Enter = 0.0001): ")
        tol = float(tol_input) if tol_input.strip() else 1e-4

        iter_input = input("Máx. iteraciones (Enter = 100): ")
        max_iter = int(iter_input) if iter_input.strip() else 100

        raiz = biseccion(f_usuario, a, b, tol, max_iter)

        if raiz is not None:
            print(f"\n Raíz aproximada: {raiz:.6f}")

    except ValueError:
        print("\n Error: Debe ingresar valores numéricos válidos.")

    continuar = input("\n¿Desea evaluar otra función? (s/n): ").lower()
    if continuar != "s":
        print("\nPrograma finalizado.")
        break
