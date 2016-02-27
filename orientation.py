from sense_hat import SenseHat

sh = SenseHat()

from time import sleep

while True:
    p, r, y = sh.get_orientation().values()
    print("pitch=%s, roll=%s, yaw=%s" % (p, r, y))
    sleep(0.5)
