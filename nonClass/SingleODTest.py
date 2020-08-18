from od_sensor import ODSensor
from pump import PWMPump
from machine import Pin
p = PWMPump(Pin(12,Pin.OUT)) 
p.pwm.freq(1000)
od = ODSensor(25,39) #LED2 is pin 2 6#OD2 is pin 36 
count = 50

import utime
while True:
    for i in range(10):
        p.pwm.freq(2000-(200*(i+1)))
        utime.sleep(0.1)
    utime.sleep(2)
    a=[]
    for i in range(count):
        a.append(od.measure(150))
    avr = sum(a)/count
    b = 0
    for i in a:
        b += (i-avr)**2
    std = (b/count)**0.5
    se = std/count**0.5
    print("standard deviation: " + str(std))
    print("standard error: " + str(se))
    print("Average: " + str(avr))
    for i in range(10):
        p.pwm.freq(200*(i+1))
        utime.sleep(0.1)
    utime.sleep(11)
    
    
    """
    light = open("light.txt","a")
    light.write(str(avr)+" ")
    light.close()
    """