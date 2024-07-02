;Swapping of two no’s EORS (ExOR) a=a^b, b=a^b, a=a^b

PRESERVE8	
	  THUMB
	area |.text|,CODE,READONLY
  EXPORT __main

__main
	LDR R0,=0xF631024C
	LDR R1,=0x17539ABD
	EORS r0,r0,r1       ;R0^R1
	EORS R1,R0,R1		;R1^R0
	EORS R0,R0,R1		;R0^R1

stop B stop
	END