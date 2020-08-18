from od_sensor import ODSensor
from pump import PrecisionPump
from machine import Pin
import time
pp = PrecisionPump(Pin(33,Pin.OUT),Pin(27,Pin.OUT))
od = ODSensor(25,39)
count = 50
while True:
    a=[]
    for i in range(count):
        a.append(od.measure(168))
    avr = sum(a)/count
    b = 0
    for i in a:
        b += (i-avr)**2
    std = (b/count)**0.5
    se = std/count**0.5
    print("standard deviation: " + str(std))
    print("standard error: " + str(se))
    print("Average: " + str(avr))
    #13 ml in the full system
    pp.feed(13)
    time.sleep(2)