# ==========================================================
# MÉTODO DE NEWTON-RAPHSON
# Autor: Orlando José Zabala Carvajal
#C.I: 31.256.875
# Materia: Cálculo Numérico
# Descripción:
# Implementación del método de Newton-Raphson para el cálculo
# numérico de raíces de ecuaciones no lineales.
# ==========================================================

import sympy as sp


def newton_raphson(f_str, x0, tol=1e-5, max_iter=100):
    """
    Método de Newton-Raphson para aproximar raíces.

    Parámetros:
    f_str     : función en formato texto (ej: 'x**3 - x - 2')
    x0        : valor inicial
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
        print(" Error: La función no pudo interpretarse.")
        return None

    # ------------------------------------------------------
    # 3) Calcular derivada automáticamente
    # ------------------------------------------------------
    df_expr = sp.diff(f_expr, x)

    # Convertir a funciones numéricas
    f = sp.lambdify(x, f_expr, "math")
    df = sp.lambdify(x, df_expr, "math")

    print("\nFunción ingresada:")
    print("f(x) =", f_expr)
    print("f'(x) =", df_expr)

    print("\nTabla de Iteraciones:")
    print(f"{'Iter':<5}{'x_n':<15}{'f(x_n)':<15}{'Error abs':<15}")
    print("-" * 60)

    xn = x0

    for i in range(1, max_iter + 1):

        fxn = f(xn)
        dfxn = df(xn)

        # Verificación para evitar división por cero
        if dfxn == 0:
            print(" La derivada es cero. El método falla.")
            return None

        # Fórmula de Newton-Raphson
        xn_next = xn - fxn / dfxn

        error_abs = abs(xn_next - xn)

        print(f"{i:<5}{xn:<15.8f}{fxn:<15.8f}{error_abs:<15.8f}")

        # Condición de parada
        if error_abs < tol:
            print("\nConvergencia alcanzada.")
            return xn_next

        xn = xn_next

    print("\nSe alcanzó el número máximo de iteraciones.")
    return xn


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

while True:

    print("\n" + "=" * 65)
    print("        CALCULADORA - MÉTODO DE NEWTON-RAPHSON")
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
        x0 = float(input("Valor inicial x0: "))

        tol_input = input("Tolerancia (Enter = 0.0001): ")
        tol = float(tol_input) if tol_input.strip() else 1e-4

        iter_input = input("Máx. iteraciones (Enter = 100): ")
        max_iter = int(iter_input) if iter_input.strip() else 100

        raiz = newton_raphson(f_usuario, x0, tol, max_iter)

        if raiz is not None:
            print(f"\n Raíz aproximada: {raiz:.8f}")

    except ValueError:
        print("\n Error: Debe ingresar valores numéricos válidos.")

    continuar = input("\n¿Desea evaluar otra función? (s/n): ").lower()
    if continuar != "s":
        print("\nPrograma finalizado.")
        break
