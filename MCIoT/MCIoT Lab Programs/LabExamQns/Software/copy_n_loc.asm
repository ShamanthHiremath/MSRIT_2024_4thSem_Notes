;Copy "n" locations      


	PRESERVE8 ; Indicate the code here preserve  
; 8 byte stack alignment         
	THUMB     ; Indicate THUMB code is used       
	AREA    |.text|, CODE, READONLY
	EXPORT __main			 
; Start of CODE area 

__main 	
	LDR r0,=0x00000000  ; Source address
	LDR r1,=0x20000000  ; Destination address
	LDR r2,=10          ; n = number of bytes to copy
copy_loop
	LDRB r3, [r0]   ; read 1 byte
	ADDS r0, r0, #1 ; increment source pointer
	STRB r3, [r1]   ; write 1 byte
	ADDS r1, r1, #1 ; increment destination pointer
	SUBS r2, r2, #1 ; decrement loop counter
	BNE copy_loop   ; loop until all data copied
stop B stop
	END