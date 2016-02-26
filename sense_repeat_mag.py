from sense_hat import SenseHat

from time import sleep

import math

sense = SenseHat()

sense.clear(0,0,0,)

while True:
    sleep(1)
    sense.show_message(" %s mag" % (math.ceil((sense.get_compass)())))
    
