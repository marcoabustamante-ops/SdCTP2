.global operacion_asm
.type operacion_asm, @function

operacion_asm:
    pushq   %rbp
    movq    %rsp, %rbp

    cvttss2si %xmm0, %eax
    addl    $1, %eax

    popq    %rbp
    ret

.section .note.GNU-stack,"",@progbits
