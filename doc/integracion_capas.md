# Documentación de Integración: Capa Superior e Intermedia

Este documento detalla la arquitectura del sistema para la **Interacción 1** y presenta los componentes necesarios para la **Interacción 2**.

---

## 1. Interacción Actual (Python + C)

En esta fase, el sistema valida la comunicación entre el lenguaje de alto nivel y la lógica de negocio en C.

* **Capa Superior (`api_gini.py`)**
  * Utiliza la librería `requests` para consumir la API del Banco Mundial.
  * Filtra los datos de **Argentina** entre los años **2011-2020**.
  * Retorna un valor `float` (índice GINI más reciente).
  * **Integración**: Mediante la librería `ctypes`, carga el objeto binario `libredondear.so` y mapea la función de C para ser usada desde Python.

* **Capa Intermedia (`redondear1.c`)**
  * Recibe el parámetro como un `float` estándar de C.
  * Realiza un casteo a entero y suma una unidad (`n = n + 1`).
  * Devuelve el resultado a la Capa Superior para su visualización.

---

## 2. Proyección para la Interacción 2 (Assembler + Stack)

Los archivos adicionales en `/src` (`api_gini_asm.py`, `redondear2.c`) están diseñados para la siguiente iteración del TP.

### Objetivos de la Interacción 2:

1. **Uso del Stack**: Implementación de **System V AMD64 ABI** para pasar argumentos y retornar valores entre C y ASM.
2. **Capa de Bajo Nivel (ASM)**: Se integrarán rutinas en Assembler x86-64 para el cálculo final.
3. **Depuración con GDB**: Uso del depurador para validar el estado del **Stack Frame** y registros (%rax, %rdi, etc.).

