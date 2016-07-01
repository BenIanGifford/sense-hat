from sense_hat import SenseHat
import matplotlib.pyplot as plt
import matplotlib.dates as md
from time import sleep
import datetime
print("To exit and graph this data hit ctrl + c")

sh = SenseHat()
temps = []
times = []

def graph():
    #times = [value for value in range(len(temps))]
    plt.xticks(rotation=25)
    plt.ylabel("Tmperature", fontsize=14)
    plt.xlabel("Time")
    ax = plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    plt.plot(times, temps)
    plt.show()
    
try:    
    while True:
        sleep(10)
        now = datetime.datetime.now()
        times.append(now)
        temp = sh.get_temperature()
        temps.append(temp)
except KeyboardInterrupt:
    print("Ploting...")
    graph()
