.global operacion_asm
.type operacion_asm, @function

operacion_asm:
    # --- PRÓLOGO ---
    pushq   %rbp
    movq    %rsp, %rbp

    # --- LÓGICA DE CONVERSIÓN Y SUMA ---
    # El float llega en %xmm0. Convertimos a entero (truncando) y guardamos en %eax.
    cvttss2si %xmm0, %eax

    # Sumamos 1 al resultado.
    addl    $1, %eax

    # --- EPÍLOGO ---
    popq    %rbp
    ret
.section .note.GNU-stack,"",@progbits
