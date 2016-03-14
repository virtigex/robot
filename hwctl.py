

class Leds:

    def __init__(self):
        self.nohw = True
        self.pinmap = [38, 40, 15, 16, 18, 22, 37, 13]
        try:
            from RPi import GPIO
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(11, GPIO.OUT)
            for pin in self.pinmap:
                GPIO.setup(pin, GPIO.OUT)
            self.nohw = False
            print('hardware control on')
        except Exception as e:
            print('cannot run without GPIO', e)

        pass

    # state is an array of eight booleans
    def led(self, state):
        from RPi import GPIO
        for pin, s in zip(self.pinmap, state):
            level = GPIO.LOW
            if s:
                level = GPIO.HIGH
            GPIO.output(pin, level)

    # set led accordin to bits in number
    def ledfromint(self, val):
        state = []
        v = val
        for i in range(len(self.pinmap)):
            if (v & 1) == 0:
                state.append(False)
            else:
                state.append(True)
            v = v >> 1
        self.led(state)

    def ledon(self):
        if self.nohw:
            return
        pass
        from RPi import GPIO
        GPIO.output(11, GPIO.HIGH)

    def ledoff(self):
        if self.nohw:
            return
        from RPi import GPIO
        GPIO.output(11, GPIO.LOW)

    def destroy(self):
        if self.nohw:
            return
        from RPi import GPIO
        GPIO.cleanup()

if __name__ == '__main__':
    leds = Leds()
    leds.ledon()
