#ifndef DACI2C__H
#define DACI2C__H

#include <Arduino.h>
#include <Wire.h>
 
int setVoltage(float valor, float vdd, int direccion);
int setVoltageMemory(float valor, float vdd, int direccion);
float getVoltageMemory(float vdd, int direccion);


#endif
