from od_sensor import ODSensor
import utime
from temp_control import T_control
t_control = T_control(14,32,12,34) #LED2 is pin 26
od1 = ODSensor(25,39) #OD2 is pin 36
count = 100



t0 = utime.time()

import utime
while True:
    t_control.pump.pwm.freq(0)
    utime.sleep(1)
    
    a=[]
    for i in range(count):
        a.append(od1.measure(150))
    avr = sum(a)/count
    b = 0
    for i in a:
        b += (i-avr)**2
    std = (b/count)**0.5
    se = std/count**0.5
    print("Average: " + str(avr))
    
    
    light = open("light.txt","a")
    light.write(str(avr)+" ")
    light.close()
    
    temp = open("temp.txt","a")
    temp.write(str(t_control.thermometer.read())+" ")
    temp.close()
    
    time = open("temp.txt","a")
    time.write(str(utime.time()-t0)+" ")
    time.close()
    
    
    t_control.call()
    utime.sleep(57)