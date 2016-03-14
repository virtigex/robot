from RPi import GPIO

def init():
    GPIO.setmode(GPIO.BOARD)


def shutdown():
    GPIO.cleanup()

class Servo:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.p = None

    def level(self, lvl):
        if self.p == None:
            self.p = GPIO.PWM(self.pin, 50)
            self.p.start(lvl)
        else:
            self.p.ChangeDutyCycle(lvl)


    def destroy(self):
        if self.p != None:
            self.p.stop()


if __name__ == '__main__':
    import time
    init()
    s = Servo(11)
    try:
        while True:
            s.level(2)
            time.sleep(4)
            s.level(5)
            time.sleep(4)
            s.level(10)
            time.sleep(4)
    except Interrupt:
        s.destroy()
        shutdown()
