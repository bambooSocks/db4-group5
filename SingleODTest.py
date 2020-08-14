from od_sensor import ODSensor

od = ODSensor()
count = 50
"""
a=0
for i in range(50):
    a += od.measure(178)
print(a/50)

a=0
for i in range(50):
    a += od.measure(255)
print(a/50)
"""
import utime
while True:
    a=[]
    for i in range(count):
        a.append(od.measure(180))
    avr = sum(a)/count
    b = 0
    for i in a:
        b += (i-avr)**2
    std = (b/count)**0.5
    se = std/count**0.5
    print("standard deviation: " + str(std))
    print("standard error: " + str(se))
    print("Average: " + str(avr))
    f.write(" ")
    f.write(str(avr))
    utime.sleep(1)

a=[]
for i in range(count):
    a.append(od.measure(255))
avr = sum(a)/count
b = 0
for i in a:
    b += (i-avr)**2
std = (b/count)**0.5
se = std/count**0.5
print("standard deviation: " + str(std))
print("standard error: " + str(se))
print("Average: " + str(avr))
