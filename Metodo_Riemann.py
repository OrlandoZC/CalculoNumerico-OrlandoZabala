# ==========================================================
# MÉTODO DE SUMAS DE RIEMANN
# Autor: Orlando José Zabala Carvajal
# C.I: 31.256.875
# Materia: Cálculo Numérico
# Descripción:
# Implementación del método de Sumas de Riemann para la
# aproximación numérica de integrales definidas.
# ==========================================================

import sympy as sp


def riemann(f_str, a, b, n, opcion):
    """
    Método de Sumas de Riemann para aproximar integrales definidas.

    Parámetros:
    f_str  : función en formato texto (ej: 'x**2 + 3*x')
    a      : límite inferior
    b      : límite superior
    n      : número de subintervalos
    opcion : 1 (Izquierda), 2 (Derecha), 3 (Punto Medio)

    Retorna:
    Aproximación de la integral o None si falla.
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
    # 3) Cálculo de Δx
    # ------------------------------------------------------
    delta_x = (b - a) / n
    suma = 0

    print("\nTabla de Subintervalos:")
    print(f"{'i':<5}{'x_i':<15}{'f(x_i)':<15}")
    print("-" * 40)

    # ------------------------------------------------------
    # 4) Aplicación del método seleccionado
    # ------------------------------------------------------
    for i in range(n):

        if opcion == 1:       # Izquierda
            xi = a + i * delta_x

        elif opcion == 2:     # Derecha
            xi = a + (i + 1) * delta_x

        elif opcion == 3:     # Punto Medio
            xi = a + (i + 0.5) * delta_x

        else:
            print(" Opción inválida.")
            return None

        fx = f(xi)
        suma += fx

        print(f"{i:<5}{xi:<15.6f}{fx:<15.6f}")

    return suma * delta_x


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

while True:

    print("\n" + "=" * 65)
    print("        CALCULADORA - MÉTODO DE SUMAS DE RIEMANN")
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
    print("   x**2 + 3*x - 1")
    print("   sin(x)")
    print("   exp(x)")
    print("-" * 65)

    f_usuario = input("Ingrese f(x): ")

    try:
        a = float(input("Límite inferior (a): "))
        b = float(input("Límite superior (b): "))
        n = int(input("Número de subintervalos (n): "))

        if n <= 0:
            print(" Error: n debe ser mayor que 0.")
            continue

        print("\nSeleccione el método:")
        print("1 - Izquierda")
        print("2 - Derecha")
        print("3 - Punto Medio")

        opcion = int(input("Opción: "))

        resultado = riemann(f_usuario, a, b, n, opcion)

        if resultado is not None:

            # Integral exacta
            x = sp.symbols('x')
            integral_exacta = sp.integrate(sp.sympify(f_usuario), (x, a, b))
            valor_exacto = float(integral_exacta)

            error_absoluto = abs(valor_exacto - resultado)

            if valor_exacto != 0:
                error_relativo = error_absoluto / abs(valor_exacto)
            else:
                error_relativo = 0

            print("\n" + "-" * 50)
            print("RESULTADOS")
            print("-" * 50)
            print(f"Integral exacta  : {valor_exacto:.8f}")
            print(f"Aproximación     : {resultado:.8f}")
            print(f"Error absoluto   : {error_absoluto:.8f}")
            print(f"Error relativo   : {error_relativo:.8f}")

    except ValueError:
        print("\n Error: Debe ingresar valores numéricos válidos.")

    continuar = input("\n¿Desea evaluar otra función? (s/n): ").lower()
    if continuar != "s":
        print("\nPrograma finalizado.")
        break
