#include <Arduino.h>
#include <Wire.h>
#include "dac_i2c.h"

#define DAC_MAX_VALUE 4096

int setVoltage(float value, float vdd, int address){
  if(value > vdd or value < 0)
	  return 2;
  value = value * DAC_MAX_VALUE / vdd;
  if (value < 0)
	  value = 0;
  else if (value == DAC_MAX_VALUE)
    value = DAC_MAX_VALUE - 1;
  value = round(value);
  int valueint = value;
  unsigned char bit1 = valueint;
  unsigned char bit2 = (valueint>>8);
  bit2 &= 0x0F;
  Wire.beginTransmission(address);
  Wire.write(bit2);
  Wire.write(bit1);
  Wire.write(bit2);
  Wire.write(bit1);
  return (Wire.endTransmission() > 0);
}

int setVoltageMemory(float value, float vdd, int address){
  if(value > vdd or value < 0)
	  return 2;
  value = value * DAC_MAX_VALUE / vdd;
  if (value < 0)
	  value = 0;
  else if (value == DAC_MAX_VALUE)
    value = DAC_MAX_VALUE - 1;
  value = round(value);
  int valueint = value;
  unsigned char bit1 = 0x60;
  unsigned char bit2 = (valueint >> 4);
  unsigned char bit3 = (valueint << 4);
  Wire.beginTransmission(address);
  Wire.write(bit1);
  Wire.write(bit2);
  Wire.write(bit3);
  return (Wire.endTransmission() > 0);
}

float getVoltageMemory(float vdd, int address){
  unsigned char bit1, bit2;
  if(!Wire.requestFrom(address, 6, true))
    return -1;
  Wire.read();
  Wire.read();
  Wire.read();
  bit1 = Wire.read();
  bit2 = Wire.read();
  int valueint = (bit1 & 0x0F) << 8 | bit2;
  return (double) valueint * vdd / DAC_MAX_VALUE;
}
