from sense_hat import SenseHat

from time import sleep

import math

sh = SenseHat()

def tempf():
    sh.show_message(" %s F" % round(sh.get_temperature() * 1.8 + 32))
    sleep(1)
    
while True:
    tempf()
