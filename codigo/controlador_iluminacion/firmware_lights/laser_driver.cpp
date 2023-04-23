#include <Arduino.h>
#include "laser_driver.h"
#include "dac_i2c.h"
#include "light_driver.h"


LaserDriver::LaserDriver(int address, float vdd, float currentVoltageFactor, int enablePin, int alwaysPin):
                         LightDriver(enablePin, alwaysPin),
                         address(address), vdd(vdd),
                         currentVoltageFactor(currentVoltageFactor) {}

float LaserDriver::currentToVoltage(float current) {
    return current / currentVoltageFactor;
}

float LaserDriver::voltageToCurrent(float voltage){
    return voltage * currentVoltageFactor;
}

int LaserDriver::setCurrent(float current) {
    float voltage = currentToVoltage(current);
    return setVoltageMemory(voltage, vdd, address);
}

float LaserDriver::getCurrent(){
    float voltage = getVoltageMemory(vdd, address);
    if (voltage < 0)
        return -1;
    return voltageToCurrent(voltage);
}

float LaserDriver::getMaxCurrent() {
    return vdd * currentVoltageFactor;
}

float LaserDriver::getMinCurrent() {
    return 0;
}
