from sense_hat import SenseHat

sh = SenseHat()

from time import sleep

while True:
    x, y, z = sh.get_accelerometer_raw().values()

    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)

    print ("x=%s, y=%s, z=%s" % (x, y, z))
