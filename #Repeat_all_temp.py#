#!/usr/bin/env python

from sense_hat import SenseHat
from time import sleep
import math

sh = SenseHat()

def shtempf():
    sh.show_message(" %s F" % round(sh.get_temperature() * 1.8 + 32))
    sleep(1)

def cputempf():
    f = open("/sys/class/thermal/thermal_zone0/temp")
    CPUTemp = f.read()
    f.close() 
    StringToOutput= str(int(CPUTemp)/1000.0 * 1.8 + 32)
    sh.show_message("CPU %s F" %StringToOutput)

while True:
    shtempf()
    cputempf()
