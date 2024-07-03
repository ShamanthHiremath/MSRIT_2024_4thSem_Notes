#include <stdio.h>
#include "NUC1xx.h"
#include "Driver\DrvGPIO.h"
#include "Driver\DrvUART.h"
#include "Driver\DrvSYS.h"
#include "NUC1xx-LB_002\LCD_Driver.h"

void LCDcallbackINT0(){
	print_lcd(0, "Smpl_LCD_Text   ");
	DrvSYS_Delay(2000000);
	clr_all_panel();
}
void LEDcallbackINT1(){
	DrvGPIO_ClrBit(E_GPC, 12); 
	DrvSYS_Delay(300000);	   
	DrvGPIO_SetBit(E_GPC, 12); 
	DrvSYS_Delay(300000);
}

/*
you have that small wire right connecting that to GPC14 and GND you will get the LCD if you remove that wire and press interrupt button LED will blink thats why we are not locking register so that interrupt can be awaked anytime
*/

int main (void){

	UNLOCKREG();
	DrvSYS_Open(48000000);

	DrvGPIO_Open(E_GPC, 12, E_IO_OUTPUT);
	DrvGPIO_SetBit(E_GPC, 12);	
	
   	Initial_panel();
	clr_all_panel();

	DrvGPIO_Open(E_GPB, 15, E_IO_INPUT);
	DrvGPIO_Open(E_GPB, 14, E_IO_INPUT);
    DrvGPIO_EnableEINT1(E_IO_BOTH_EDGE, E_MODE_EDGE, LEDcallbackINT1);
	DrvGPIO_EnableEINT0(E_IO_BOTH_EDGE, E_MODE_EDGE, LCDcallbackINT0); 
  	while(1){
		// kaali
  	}
	return 0;
}