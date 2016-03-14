from time import sleep
import signal
import sys
import threading
import hwctl
import os

global thr
thr = None

class pattern1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.do_run = True

    def run(self):
        leds = 1
        l = hwctl.Leds()
        self.do_run = True
        while self.do_run:
            sleep(0.1)
            leds = leds << 1
            l.ledfromint(leds)
            if leds >= 256:
                leds = 1
        l.ledfromint(0)
        l.destroy()
        print('test finished')

    def stop(self):
        self.do_run = False
        self.join()

def handler(signum, frame):
    global thr
    thr.do_run = False

def main():
    global thr
    signal.signal(signal.SIGTERM, handler)
    thr = pattern1()
    pid = os.getpid()
    with (open('pattern.id', 'w')) as f:
        f.write(str(pid))
    try:
        thr.run()
    except KeyboardInterrupt:
        print('terminated')

if __name__ == '__main__':
	main()

