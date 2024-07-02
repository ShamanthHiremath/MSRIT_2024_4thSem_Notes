;Factorial of a number

    PRESERVE8                ; Indicate the code here preserves 8-byte stack alignment
    THUMB                   ; Indicate THUMB code is used
    AREA    |.text|, CODE, READONLY
    EXPORT  main            ; Export the main symbol

main
    movs r0, #5          ; Initialize r0 with 5 (the number to calculate the factorial of)
    movs r1, r0          ; Initialize r1 with the value in r0 (r1 will hold the result)
    subs r0, r0, #1      ; Decrement r0 by 1 (prepare for the loop)

loop
    muls  r1, r1, r0      ; Multiply r1 by r0 and store the result in r1
    subs  r0, r0, #1      ; Decrement r0 by 1
    bne   loop            ; Branch to loop if the result of the subtraction is not zero

    ; The result (factorial) is now in r1
    bx lr              ; Return from main
stop b stop
end
             
             ;OR

             PRESERVE8 ; Indicate the code here preserve  
; 8 byte stack alignment         
                     THUMB     ; Indicate THUMB code is used       
                 AREA    |.text|, CODE, READONLY		   
              EXPORT __main			 
; Start of CODE area 
__main
       movs r2,#1
       movs r0,#5
	   cmp r0,#0
	   beq result
	   movs r1,r0
loop   muls r2,r1,r2
       subs r1,r1,#1
	   cmp r1,#0
	   bgt loop
result b result
       END