    PRESERVE8 ; Indicate the code here preserve  
    THUMB     ; Indicate THUMB code is used       
    AREA    |.text|, CODE, READONLY
	EXPORT __main 
    EXTERN  func1
; Start of CODE area

__main
	LDR r0,=0x10;
    BL func1
stop B stop
  END