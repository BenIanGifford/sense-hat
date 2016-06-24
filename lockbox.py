disclamer = """You should not use this program to store any actully important data
it is intended as an interesting program to demonstrate the cababilitys of the sense hat
and should not be used in any other way"""

### imports ###
from sense_hat import SenseHat
from time import sleep

### variables ###

unlocked1 = False
unlocked2 = False

sh = SenseHat()
e = (0,0,0)
r = (255,0,0)
g = (0,255,0)
w = (255,255,255)

locked_screen = [
e,e,e,e,e,e,e,e,
e,e,e,w,w,e,e,e,
e,e,w,e,e,w,e,e,
e,e,w,e,e,w,e,e,
e,e,r,r,r,r,e,e,
e,e,r,r,r,r,e,e,
e,e,r,r,r,r,e,e,
e,e,e,e,e,e,e,e
]

unlocked_screen = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,w,w,e,
e,e,e,e,w,e,e,w,
e,e,e,e,w,e,e,w,
e,e,g,g,g,g,e,e,
e,e,g,g,g,g,e,e,
e,e,g,g,g,g,e,e,
e,e,e,e,e,e,e,e
]
    
sh.set_pixels(locked_screen)


def unlock():
    sh.set_pixels(unlocked_screen)
    sleep(2)
    sh.show_message("You have unlocked it!! This is a secret message")

while True:
    if round(sh.get_humidity()) >= 50: 
        unlocked1 = True
    if unlocked1 == True and round(sh.get_temperature()) >= 26:
        unlocked2 = True
        unlock()
        quit()
