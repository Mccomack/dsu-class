import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

display = bundle.displays[0]
led = bundle.leds[0]
speaker = bundle. speakers [0]

def jupasu(tune, much):
    speaker.tune = tune, 100  #(주파수, 볼륨)
    time.sleep(much)

def shee(much):
    speaker.tune = 0, 100
    time.sleep(much)

class traffic:
    def __init__(self):
        self.prev = False

    def green(self):
        led.rgb = (0, 0, 255)
        display.text = "walk"
        jupasu(523, 0.1)
        shee(0.1)
        jupasu(523, 0.1)
        shee(0.1)

    def red(self):
        led.rgb = (255, 0, 0)
        display.text = "stop"
        # jupasu(523, 0.1)
        # shee(0.1)
        # jupasu(523, 0.1)
        # shee(0.1)

    def yellow(self):
        led.rgb = (255, 255, 0)
        display.text = "wait"
    
    def change(self):
        if self.prev:
            self.yellow()
            time.sleep(1)
            self.red()
        else:
            self.yellow()
            time.sleep(1)
            self.green()
        self.prev = not(self.prev)



t1 = traffic()
t1.change()
time.sleep(5)
t1.change()
time.sleep(5)

led.turn_off()
speaker.reset()