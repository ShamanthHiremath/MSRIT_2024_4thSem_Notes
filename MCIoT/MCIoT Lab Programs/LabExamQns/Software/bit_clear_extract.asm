    PRESERVE8               ; Indicate the code here preserves 8-byte stack alignment
    THUMB                   ; Indicate THUMB code is used
    AREA    |.text|, CODE, READONLY
    EXPORT  __main          ; Export the __main symbol

; Start of CODE area
__main
    ; Extracting bits of width W and start position S
    LDR     r0, =0xFFC0FFFF  ; Load the value 0xFFC0FFFF into register r0
    LSLS    r0, r0, #(32-16-8) ; Logical shift left r0 by (32-16-8) bits (32-W-S)
    LSRS    r0, r0, #(32-8)  ; Logical shift right r0 by (32-8) bits 

    ; Clearing bits
    LDR     r0, =0xFFC0FFFF  ; Reload the value 0xFFC0FFFF into register r0
    MOVS    r1, #16          ; Load 16 into register r1
    MOVS    r2, #8           ; Load 8 into register r2  ;(32-16-08)//(32-W-S)
    MOVS    r3, #8           ; Load 8 into register r3
    RORS    r0, r0, r1       ; Rotate right r0 by 16 bits
    LSRS    r0, r0, r2       ; Logical shift right r0 by 8 bits
    RORS    r0, r0, r3       ; Rotate right r0 by 8 bits

stop    B   stop             ; Infinite loop to stop the program

    END                      ; End of the program
