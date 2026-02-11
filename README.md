# Repositorio de Algoritmos - Cálculo Numérico

## Descripción del Proyecto

Este repositorio contiene las implementaciones de métodos numéricos desarrollados para la asignatura **Cálculo Numérico** durante el período académico actual.

El propósito de este espacio es servir como registro técnico y académico de los algoritmos utilizados para:

* La resolución de ecuaciones no lineales.
* La aproximación numérica de integrales definidas.
* El análisis de error en métodos iterativos.

Cada implementación ha sido estructurada siguiendo criterios de claridad, documentación formal y consistencia en el estilo de programación.

---

## Contenido Técnico

El repositorio se organiza mediante scripts independientes diseñados para abordar problemas específicos del cálculo numérico:

| Archivo                  | Descripción del Método                                                                          |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| Método Bisección.py      | Búsqueda de raíces mediante partición de intervalos basada en el Teorema de Bolzano.            |
| Método Newton-Raphson.py | Aproximación de raíces utilizando derivadas y método iterativo de convergencia cuadrática.      |
| Método Riemann.py        | Cálculo de integrales definidas mediante sumas de Riemann por izquierda, derecha y punto medio. |

---

## Descripción de los Métodos Implementados

### Método de Bisección

Implementación basada en el Teorema de Bolzano, que garantiza la existencia de una raíz si existe cambio de signo en un intervalo cerrado.

Características principales:

* Verificación de condición f(a) · f(b) < 0.
* Tabla detallada de iteraciones.
* Cálculo de error absoluto.
* Cálculo de error teórico (cota máxima garantizada).
* Control de tolerancia y número máximo de iteraciones.
* Validación de errores mediante estructuras try/except.

---

### Método de Newton-Raphson

Método iterativo basado en la derivada de la función:

xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)

Características principales:

* Derivación automática usando SymPy.
* Conversión simbólica a función numérica.
* Tabla de iteraciones con error absoluto.
* Control de división por cero.
* Condición de parada por tolerancia.
* Manejo de número máximo de iteraciones.

---

### Método de Sumas de Riemann

Implementación para aproximar integrales definidas mediante:

* Suma izquierda.
* Suma derecha.
* Punto medio.

Características principales:

* Cálculo automático de Δx.
* Tabla de subintervalos.
* Comparación con la integral exacta mediante SymPy.
* Cálculo de error absoluto y error relativo.
* Evaluación simbólica y numérica integrada.

---

## Especificaciones de Desarrollo

Para la ejecución de los scripts se utilizaron los siguientes recursos técnicos:

* Lenguaje de programación: Python 3
* Librería utilizada: SymPy
* Tipo de interfaz: Consola interactiva
* Funcionalidad adicional:

  * Tablas formateadas de iteraciones.
  * Validación de entradas.
  * Cálculo automático de errores.
  * Derivación simbólica automática (Newton-Raphson).
  * Integración simbólica automática (Riemann).

---

## Información del Autor

Nombre: Orlando Zabala
Identificación: C.I: 31.256.875
Asignatura: Cálculo Numérico

---
