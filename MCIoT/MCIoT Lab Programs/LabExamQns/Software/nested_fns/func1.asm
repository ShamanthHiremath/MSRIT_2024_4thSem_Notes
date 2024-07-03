PRESERVE8
	THUMB
	AREA |.text|, CODE, READONLY
	EXPORT func1
	EXTERN func2
	
func1
	push{LR}
	MOVS R1,#08
	BL func2
	pop{PC}
stop b stop
	END