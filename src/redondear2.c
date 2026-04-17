// Declaramos la función externa que escribiste en Ensamblador
extern int operacion_asm(float valor);

// La función que será invocada desde Python vía ctypes
int redondear(float valor) {
    // C actúa como puente y le pasa el float a la capa de ASM
    return operacion_asm(valor); 
}
