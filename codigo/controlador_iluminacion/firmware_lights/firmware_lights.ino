#include <Wire.h>
#include "dac_i2c.h"
#include "light_driver.h"
#include "laser_driver.h"

#define LASER_ADDRESS 0b01100010
#define LASER_ENABLE_PIN 7
#define LED_ENABLE_PIN 6
#define LED_ALWAYS_PIN 5
#define LASER_ALWAYS_PIN 4

#define VDD 5
#define LASER_CURRENT_VOLTAGE_FACTOR 20.83

// codigos de respuesta como numeros.
#define CODE_OK 'A'
#define CODE_COMM_ERROR 'B'
#define CODE_BAD_INPUT 'C'
#define CODE_NO_CMD 'D'

// codigos de entrada como letras.
#define CMD_LASER_SET_CURRENT 'A'
#define CMD_LASER_GET_CURRENT 'B'
#define CMD_LASER_GET_MAX_CURRENT 'C'
#define CMD_LASER_GET_MIN_CURRENT 'D'
#define CMD_LASER_ENABLE 'J'
#define CMD_LASER_DISABLE 'K'
#define CMD_LASER_GET_STATE 'L'
#define CMD_LASER_ALWAYS_ON 'M'
#define CMD_LASER_ALWAYS_OFF 'N'
#define CMD_LED_ENABLE 'O'
#define CMD_LED_DISABLE 'P'
#define CMD_LED_ALWAYS_ON 'Q'
#define CMD_LED_ALWAYS_OFF 'R'
#define CMD_LED_GET_STATE 'S'
#define CMD_LASER_GET_ALWAYS_STATE 'T'
#define CMD_LED_GET_ALWAYS_STATE 'U'

LaserDriver laserDriver = LaserDriver(LASER_ADDRESS, VDD, LASER_CURRENT_VOLTAGE_FACTOR, LASER_ENABLE_PIN, LASER_ALWAYS_PIN);
LightDriver ledDriver = LightDriver(LED_ENABLE_PIN, LED_ALWAYS_PIN);

char cmd, buffer_clean;
float value;
int state;

char cmd_readed;

void setup() {
  // Se setea i2c, el puerto serial, y el pin A0 como input.
  Wire.begin();
  Serial.begin(9600);
  //pinMode(CURRENT_SENSE_PIN, INPUT);
}

void loop() {
  //Serial.println(cmd_readed);
  if (Serial.available()){
    cmd = Serial.read();
    switch (cmd) {
      case CMD_LASER_SET_CURRENT:
        value = Serial.parseFloat();
        state =  laserDriver.setCurrent(value);
        if (state == 1)
          Serial.println(CODE_COMM_ERROR);
        else if (state == 2)
          Serial.println(CODE_BAD_INPUT);
        else
          Serial.println(CODE_OK);
        break;
      case CMD_LASER_GET_CURRENT:
        value = laserDriver.getCurrent();
        if (value < 0)
          Serial.println(CODE_COMM_ERROR);
        else {
          Serial.print(value);
          Serial.println(CODE_OK);
        }
        break;
      case CMD_LASER_GET_MAX_CURRENT:
        Serial.print(laserDriver.getMaxCurrent());
        Serial.println(CODE_OK);
        break;
      case CMD_LASER_GET_MIN_CURRENT:
        Serial.print(laserDriver.getMinCurrent());
        Serial.println(CODE_OK);
        break;
      case CMD_LASER_ENABLE:
        laserDriver.enable();
        Serial.println(CODE_OK);
        break;
      case CMD_LASER_DISABLE:
        laserDriver.disable();
        Serial.println(CODE_OK);
        break;
      case CMD_LASER_GET_STATE:
        Serial.print(laserDriver.getState());
        Serial.println(CODE_OK);
        break;
      case CMD_LASER_ALWAYS_ON:
        laserDriver.alwaysOn();
        Serial.println(CODE_OK);
        break;
      case CMD_LASER_ALWAYS_OFF:
        laserDriver.alwaysOff();
        Serial.println(CODE_OK);
        break;
      case CMD_LED_ALWAYS_ON:
        ledDriver.alwaysOn();
        Serial.println(CODE_OK);
        break;
      case CMD_LED_ALWAYS_OFF:
        ledDriver.alwaysOff();
        Serial.println(CODE_OK);
        break;
      case CMD_LED_ENABLE:
        ledDriver.enable();
        Serial.println(CODE_OK);
        break;
      case CMD_LED_DISABLE:
        ledDriver.disable();
        Serial.println(CODE_OK);
        break;
      case CMD_LED_GET_STATE:
        Serial.print(ledDriver.getState());
        Serial.println(CODE_OK);
        break;
      case CMD_LASER_GET_ALWAYS_STATE:
        Serial.print(laserDriver.getAlwaysState());
        Serial.println(CODE_OK);
        break;
      case CMD_LED_GET_ALWAYS_STATE:
        Serial.print(ledDriver.getAlwaysState());
        Serial.println(CODE_OK);
        break;
      default:
        Serial.println(CODE_NO_CMD);
        break;
    }
    while (Serial.available() > 0){
      buffer_clean = Serial.read();
    }
  }
}
