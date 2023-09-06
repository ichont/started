/*
    Paper Counter
    Copyright (C) 2022  ???

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include "reg52.h"
#include "i2c.h"

typedef unsigned char u8;
typedef unsigned int u16;

#define GPIO_DIG P0
#define AllNUM   80

sbit LSA=P2^2;
sbit LSB=P2^3;
sbit LSC=P2^4;

sbit KeyAddNum=P3^2;  //????
sbit KeySure=P3^3;  //????K4
sbit bee=P2^5;


u8 code smgduan[11]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x40};//??


u8 DisplayData[8];

unsigned char TimeCount;//?????
u16  Freq = 0; //????
u16  Freq_array[6]={0};//???????

u16  NumOfTest = 0;//?????
char Num = 0;//??????


//????
void delay(u16 i)
{
    while(i--);
}

//??????
unsigned char CalPaperNum(u16 frequence)
{
    char i;
    int freq1,num11,num12;
    int freq2,num21,num22;
    int freq3,num31,num32;
    unsigned char PaperNum;

    for(i=2; i<AllNUM-3 ;i+=2)
    {
        num11 = At24c02Read(i-2);
        delay(1000);
        num12 = At24c02Read(i-1);
        delay(1000);
        freq1 = num11*255 + num12;
        
        num21 = At24c02Read(i);
        delay(1000);
        num22 = At24c02Read(i+1);
        delay(1000);
        freq2 = num21*255 + num22;
        
        num31 = At24c02Read(i+2);
        delay(1000);
        num32 = At24c02Read(i+3);
        delay(1000);
        freq3 = num31*255 + num32;
        //??????????????????????
        if(
            (freq2 -(0.4) * (freq2 - freq1) <= frequence) 
            && (frequence < freq2 + (0.6)*(freq3 - freq2))
          ) 
        {
             PaperNum = i/2;
            return PaperNum;	
        }
         
    }
    return 0;
}

//????0&1???
void Int01_Config()
{
    //??INT0
    IT0=1;//???????(???)
    EX0=1;//??INT0??????
    //??INT1
    IT1=1;//???????(???)
    EX1=1;//??INT1??????
    PX1=1;	
}

//?????????
void Timer_Config() //????????
{
    TMOD=0x51;//???1??????,??01.???0??????,??01    ??TR0????

    TH0=0x3c;//???????,??50ms
    TL0=0xb0;

    ET0=1;//?????0????
    ET1=1;//?????1????,??
    EA=1;//?????
}

//?????
void Timer_OnOff(int ONOFF)
{
    if(ONOFF == 1)
    {
         TR0=1;//?????0,??
        TR1=1;//?????1,??
    }else
    {
         TR0=0;//?????0,??
        TR1=0;//?????1,??
    }	
}

void DigDisplay()
{
    u8 i;
    for(i=0;i<8;i++)
    {
        switch(i)	 //??,????????,
        {
            case(0):
                LSA=0;LSB=0;LSC=0; break;//???0?
            case(1):
                LSA=1;LSB=0;LSC=0; break;//???1?
            case(2):
                LSA=0;LSB=1;LSC=0; break;//???2?
            case(3):
                LSA=1;LSB=1;LSC=0; break;//???3?
            case(4):
                LSA=0;LSB=0;LSC=1; break;//???4?
            case(5):
                LSA=1;LSB=0;LSC=1; break;//???5?
            case(6):
                LSA=0;LSB=1;LSC=1; break;//???6?	
            case(7):
                LSA=1;LSB=1;LSC=1; break;//???7?	
        }
        GPIO_DIG=DisplayData[i];
        delay(100);
        GPIO_DIG=0x00;
    }
}

void main()
{

    Int01_Config();
    Timer_Config();//???0/1???
    Timer_OnOff(1);
    At24c02Write(NumOfTest,0);
    NumOfTest++;
    delay(2000);
    At24c02Write(NumOfTest,0);
    NumOfTest++;
    delay(2000);

    while(1)
    {
        if(TR1 == 0) //????200ms,?????
        {
            Freq = Freq + TL1;
            Freq = Freq + (TH1*256);
            Freq_array[0] = Freq_array[1];
            Freq_array[1] = Freq_array[2];
            Freq_array[2] = Freq_array[3];
            Freq_array[3] = Freq_array[4];
            Freq_array[4] = Freq ;

            Freq_array[5] = Freq_array[0]*0.1 + 
                            Freq_array[1]*0.1 + 
                            Freq_array[2]*0.2 + 
                            Freq_array[3]*0.3 + 
                            Freq_array[4]*0.3;

            if(Freq_array[5]==0)
            {
                bee = 0;
                delay(2000);
                bee = 1;
                delay(10);

                DisplayData[7]=smgduan[10];
                DisplayData[6]=smgduan[10];

                DisplayData[4]=smgduan[10];
                DisplayData[3]=smgduan[10];
                DisplayData[2]=smgduan[10];				
                DisplayData[1]=smgduan[10];
                DisplayData[0]=smgduan[10];//???
            }else{
                DisplayData[4]=smgduan[Freq_array[5] %100000/10000];
                DisplayData[3]=smgduan[Freq_array[5] %10000/1000];
                DisplayData[2]=smgduan[Freq_array[5] %1000/100];				
                DisplayData[1]=smgduan[Freq_array[5] %100/10];
                DisplayData[0]=smgduan[Freq_array[5] %10];//???
            }
            //??
            Freq=0;
            TH1=0;
            TL1=0;
            Timer_OnOff(1);
        }

        DigDisplay();
    } 
    
        
}

//????0?????
void Int0()	interrupt 0		
{
    delay(1000);	 //????
    if(KeyAddNum==0)
    {
        Num = CalPaperNum(Freq_array[5]);

        DisplayData[7]=smgduan[Num/10];
        DisplayData[6]=smgduan[Num%10];
            
        Timer_OnOff(0);
        bee = 0;
        delay(500);
        bee = 1;
        delay(10);
        Timer_OnOff(1);
    }
    
}

//????1?????
void Int1()	interrupt 2		
{
    delay(3000);	 //????
    if(KeySure==0)
    {
        At24c02Write(NumOfTest,Freq_array[5]/255);
        NumOfTest++;
        delay(2000);
        At24c02Write(NumOfTest,Freq_array[5]%255);
        NumOfTest++;
        delay(2000);
        bee = 0;
        delay(5000);
        bee = 1;
        delay(10);
        DisplayData[7]=smgduan[(NumOfTest/2-1)/10];
        DisplayData[6]=smgduan[(NumOfTest/2-1)%10];	
    }
    delay(1000);
}

//????1 ?????????0?????
void Timer0() interrupt 1
{
    //?????????,??50ms
    TH0 = 0x3c;
    TL0 = 0xb0;

    TimeCount++;  
    if(TimeCount == 4)//200ms
    {
        TimeCount = 0;//??
        Timer_OnOff(0);
    }
}

//????3 ?????????1?????
void Timer1() interrupt 3
{
    
}
