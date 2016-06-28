from sense_hat import SenseHat
import matplotlib.pyplot as plt
from time import sleep

print("To exit and graph this data hit ctrl + c")

sh = SenseHat()
temps = []
times = []

def graph():
    times = [value**10 for value in range(len(temps))]
    plt.ylabel("Tmperature", fontsize=14)
    plt.xlabel("Time", fontsize=14)
    plt.plot(times, temps)
    plt.show()
    
try:    
    while True:
        sleep(10)
        temp = sh.get_temperature()
        temps.append(temp)
except KeyboardInterrupt:
    print("Ploting...")
    graph()
