from sense_hat import SenseHat

from time import sleep

import math

sense = SenseHat()

sense.clear(0,0,0,)

while True:
        sense.show_message(" %s''" % round(sense.get_pressure()*0.0295301),2)
        sleep(1)
