#include <Arduino.h>
#include "laser_driver.h"
#include "dac_i2c.h"


LightDriver::LightDriver(int enablePin, int alwaysPin):
                         enablePin(enablePin), alwaysPin(alwaysPin), state(false), alwaysState(false) {
    pinMode(enablePin, OUTPUT);
    pinMode(alwaysPin, OUTPUT);
    disable();
    alwaysOff();
}

void LightDriver::enable() {
  digitalWrite(enablePin, HIGH);
  state = true;
}

void LightDriver::disable() {
  digitalWrite(enablePin, LOW);
  state = false;
}

bool LightDriver::getState() {
  return state;
}

void LightDriver::alwaysOn() {
  digitalWrite(alwaysPin, HIGH);
  alwaysState = true;
}

void LightDriver::alwaysOff() {
  digitalWrite(alwaysPin, LOW);
  alwaysState = false;
}

bool LightDriver::getAlwaysState() {
  return alwaysState;
}
