#ifndef LIGHT_DRIVER__H
#define LIGHT_DRIVER__H

#include <Arduino.h>
#include "dac_i2c.h"

class LightDriver {
protected:
    int enablePin, alwaysPin;
    bool state, alwaysState;

public:
    LightDriver(int enablePin, int alwaysPin);
    void enable();
    void disable();
    bool getState();
    void alwaysOn();
    void alwaysOff();
    bool getAlwaysState();
};



#endif
