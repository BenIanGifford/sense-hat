from sense_hat import SenseHat

sh = SenseHat()

while True:
    print([sh.get_accelerometer_raw()[key] for key in ['x','y','z']])
