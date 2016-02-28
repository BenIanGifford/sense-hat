from sense_hat import SenseHat

from time import sleep

sense = SenseHat()

sense.set_rotation(90)

sense.clear(0, 0, 0,)


while True:
    sense.show_message(" %s F" % round(sense.get_temperature() * 1.8 + 32))
    sleep(1)
    sense.show_message(" %s prh" % round((sense.get_humidity)()))
    sleep(1)
    sense.show_message(" %s''" % round((sense.get_pressure() * 0.0295301), 2))
    sleep(1)
