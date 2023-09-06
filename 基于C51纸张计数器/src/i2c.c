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

#include"i2c.h"

/*******************************************************************************
* ???         : Delay10us()
* ????		   : ??10us
* ??           : ?
* ??         	 : ?
*******************************************************************************/

void Delay10us()
{
    unsigned char a,b;
    for(b=1;b>0;b--)
        for(a=2;a>0;a--);

}
/*******************************************************************************
* ???         : I2cStart()
* ????		 : ????:?SCL??????????SDA?????????
* ??           : ?
* ??         	 : ?
* ??           : ????SDA?SCL??0
*******************************************************************************/

void I2cStart()
{
    SDA=1;
    Delay10us();
    SCL=1;
    Delay10us();//?????SDA????>4.7us
    SDA=0;
    Delay10us();//?????>4us
    SCL=0;			
    Delay10us();		
}
/*******************************************************************************
* ???         : I2cStop()
* ????		 : ????:?SCL?????????SDA?????????
* ??           : ?
* ??         	 : ?
* ??           : ??????SDA?SCL??1;??????
*******************************************************************************/

void I2cStop()
{
    SDA=0;
    Delay10us();
    SCL=1;
    Delay10us();//??????4.7us
    SDA=1;
    Delay10us();		
}
/*******************************************************************************
* ???         : I2cSendByte(unsigned char dat)
* ????		 : ??I2C????????SCL?????????,??????SDA????
* ??           : num
* ??         	 : 0?1???????1,??????0
* ??           : ???????SCL=0,SDA=1
*******************************************************************************/

unsigned char I2cSendByte(unsigned char dat)
{
    unsigned char a=0,b=0;//??255,???????1us,????255us?		
    for(a=0;a<8;a++)//???8?,??????
    {
        SDA=dat>>7;	 //??????SCL=0,????????SDA??
        dat=dat<<1;
        Delay10us();
        SCL=1;
        Delay10us();//????>4.7us
        SCL=0;
        Delay10us();//????4us		
    }
    SDA=1;
    Delay10us();
    SCL=1;
    while(SDA)//????,?????????SDA??
    {
        b++;
        if(b>200)	 //????2000us????????,??????,??????
        {
            SCL=0;
            Delay10us();
            return 0;
        }
    }
    SCL=0;
    Delay10us();
     return 1;		
}
/*******************************************************************************
* ???         : I2cReadByte()
* ????		   : ??I2c??????
* ??           : ?
* ??         	 : dat
* ??           : ???????SCL=0,SDA=1.
*******************************************************************************/

unsigned char I2cReadByte()
{
    unsigned char a=0,dat=0;
    SDA=1;			//???????????SCL??0
    Delay10us();
    for(a=0;a<8;a++)//??8???
    {
        SCL=1;
        Delay10us();
        dat<<=1;
        dat|=SDA;
        Delay10us();
        SCL=0;
        Delay10us();
    }
    return dat;		
}


/*******************************************************************************
* ???         : void At24c02Write(unsigned char addr,unsigned char dat)
* ????		   : ?24c02???????????
* ??           : ?
* ??         	 : ?
*******************************************************************************/

void At24c02Write(unsigned char addr,unsigned char dat)
{
    I2cStart();
    I2cSendByte(0xa0);//???????
    I2cSendByte(addr);//?????????
    I2cSendByte(dat);	//????
    I2cStop();
}
/*******************************************************************************
* ???         : unsigned char At24c02Read(unsigned char addr)
* ????		   : ??24c02??????????
* ??           : ?
* ??         	 : ?
*******************************************************************************/

unsigned char At24c02Read(unsigned char addr)
{
    unsigned char num;
    I2cStart();
    I2cSendByte(0xa0); //???????
    I2cSendByte(addr); //????????
    I2cStart();
    I2cSendByte(0xa1); //???????
    num=I2cReadByte(); //????
    I2cStop();
    return num;	
}

