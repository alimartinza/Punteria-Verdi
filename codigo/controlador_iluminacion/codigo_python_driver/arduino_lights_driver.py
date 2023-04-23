import serial
import time


class ArduinoLightsDriver():
    def __init__(self, port):
        self._ser = serial.Serial(port, 9600, timeout=0.001)
        time.sleep(3)
        self._update()
    
    def enable_laser(self):
        self._ser.write(bytes('J', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()
    
    def disable_laser(self):
        self._ser.write(bytes('K', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()

    def always_on_laser(self):
        self._ser.write(bytes('M', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()
    
    def always_off_laser(self):
        self._ser.write(bytes('N', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()

    def enable_led(self):
        self._ser.write(bytes('O', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()
    
    def disable_led(self):
        self._ser.write(bytes('P', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()

    def always_on_led(self):
        self._ser.write(bytes('Q', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()
    
    def always_off_led(self):
        self._ser.write(bytes('R', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()

    def set_current_laser(self, current):
        self._ser.write(bytes('A', 'UTF-8'))
        self._ser.write(bytes(str(current) + '', 'UTF-8'))
        _, code = self._receive()
        if code != "A":
            raise Exception("Error")
        self._update()

    def _get_current_laser(self):
        self._ser.write(bytes('B', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        return float(read)

    def _get_state_laser(self):
        self._ser.write(bytes('L', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        return bool(int(read))

    def _get_state_laser(self):
        self._ser.write(bytes('L', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        return bool(int(read))

    def _get_always_state_laser(self):
        self._ser.write(bytes('T', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        return bool(int(read))

    def _get_state_led(self):
        self._ser.write(bytes('S', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        return bool(int(read))

    def _get_always_state_led(self):
        self._ser.write(bytes('U', 'UTF-8'))
        read, code = self._receive()
        if code != "A":
            raise Exception("Error")
        return bool(int(read))

    def _update(self):
        self._current = self._get_current_laser()
        self._state_laser = self._get_state_laser()
        self._always_state_laser = self._get_always_state_laser()
        self._state_led = self._get_state_led()
        self._always_state_led = self._get_always_state_led()

    def _receive(self):
        received = ""
        self._wait_until_receive()
        while self._ser.inWaiting() and (not received or received[-1] != '\n'):
            received += self._ser.read(1).decode('UTF-8')
        if not received:
            raise Exception("Nothing received")
        received = received.replace("\n", "")

        return received[0:-2], received[-2]

    def _wait_until_receive(self):
        while not self._ser.inWaiting():
            time.sleep(0.1)

    @property
    def current(self):
        return self._current

    @property
    def laser_is_enabled(self):
        return self._state_laser

    @property
    def laser_is_always_on(self):
        return self._always_state_laser

    @property
    def led_is_enabled(self):
        return self._state_led

    @property
    def led_is_always_on(self):
        return self._always_state_led

    
