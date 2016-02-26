from sense_hat import SenseHat

sh = SenseHat()

from time import sleep

#sh.show_letter("I")

# set up the colours (white, green, red, empty)

w = [150, 150, 150]
g = [0, 255, 0]
r = [255, 0, 0]
e = [0, 0, 0]

# create images for three different coloured arrows

arrow = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,e,w,w,e,w,e,
w,e,e,w,w,e,e,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e
]

# Print it once
sh.set_pixels(arrow)

while True:
    x_full, y_full, z_full = sh.get_accelerometer_raw().values()

    x=round(x_full, 0)
    y=round(y_full, 0)
    z=round(z_full, 0)

    print ("x=%s, y=%s, z=%s" % (x_full,y_full,z_full))

    if x == -1:  # works
        sh.set_pixels(arrow)
        sh.set_rotation(180)
    elif x == 1: # works
        sh.set_pixels(arrow)
        sh.set_rotation(0)
        
    elif y == 1: 
        sh.set_pixels(arrow)
        sh.set_rotation(270)
    elif y == -1:
        sh.set_pixels(arrow)
        sh.set_rotation(90)
    else:
        sh.show_letter("*")
