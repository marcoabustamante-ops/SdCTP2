# Documentación de Integración: Capa Superior, Capa Intermedia y Capa de Bajo Nivel (Assembler)

Este documento detalla la arquitectura del sistema implementado para el TP2 de Sistemas de Computación, enfocándose en la interacción entre las capas de Python, C y la implementación en Assembler. Se describen las funciones de cada capa, cómo se comunican entre sí en ambas iteraciones del TP


---

## 1. Interacción 1 (Python + C)

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

## 2.Interacción 2 (Python + C + Assembler)

El flujo de ejecucion sigue una arquitectura descendente de tres capas, donde cada capa va delegando responsabilidades a la siguiente capa inferior, siguiendo el principio de separación de responsabilidades y modularidad:

* **Capa Superior (`api_gini_asm.py`)**
  * Mantiene la logica de consumo de la API del Banco Mundial y el filtrado de datos.
  * La integracion con ctypes se mantiene, pero ahora llama a libredondear2.so, que vincula internamente con los dos lenguajes de bajo nivel (C y ASM).

* **Capa Intermedia (`redondear2.c`)**
  * Actua como wrapper entre Python y Assembler, recibiendo el valor `float` desde Python.
  * Decalra la existenia de la funcion  externa: `extern int operacion_asm(float valor);.` que se implementa en Assembler.
  * Su función principal es pasar el valor a la capa de bajo nivel (Assembler) y retornar el resultado a Python.

* **capa de Bajo Nivel (operacion_asm.s)**
  * Maneja la conversión de `float` a `int` y hace le suma uno al resultado utilizando instrucciones específicas de x86-64.
  * Utiliza el registro `xmm0` para recibir el valor `float` desde C, y el registro `eax` para retornar el resultado entero a la capa intermedia.
  * Mediante el uso de las intrucciones de conversión de punto flotante a entero (`cvttss2si`) y la suma utilaza la instrucción `add`, se realizando la operación requerida.
  * Retorna el resultado a la capa intermedia, que a su vez lo devuelve a la capa superior para su presentación.
  * sigue el estándar de llamadas **System V AMD64 ABI** para la comunicación entre C y ASM, utilizando el stack para pasar argumentos y retornar valores.

### Debugging con GDB

Para depurar la función en Assembler, se uso el depurador GDB, enfocándose en el área de memoria del stack antes, durante y después de la ejecución de la función `operacion_asm`. Esto permitió verificar que los argumentos se pasaban correctamente y que el resultado se almacenaba adecuadamente en el registro de retorno.
Mediante la inspeccion de las direcciones, se verifico el correcto almacenamiento de los valores en el stack y el correcto retorno del resultado a la capa intermedia. Tambien se valido que el argumento de punto flotante 'float' se pasaba correctamente a través del registro `xmm0`, y que el resultado entero se retornaba a través del registro `eax` siguiendo el estándar de llamadas. Esto garantizo la correcta integración entre las capas y el funcionamiento esperado del sistema en su conjunto.

 **Nota:** El detalle técnico del volcado de memoria y los registros mencionados puede consultarse en el archivo adjunto `resultados_gdb.txt`, que contiene la salida del depurador durante la ejecución de la función en Assembler.