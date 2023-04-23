#ifndef LASER_DRIVER__H
#define LASER_DRIVER__H

#include <Arduino.h>
#include "dac_i2c.h"
#include "light_driver.h"

class LaserDriver : public LightDriver {
    int address;
    float vdd, currentVoltageFactor;

    float currentToVoltage(float current);
    float voltageToCurrent(float voltage);

public:
    LaserDriver(int address, float vdd, float currentVoltageFactor, int enablePin, int alwaysPin);
    int setCurrent(float current);
    float getCurrent();
    float getMaxCurrent();
    float getMinCurrent();
};



#endif
