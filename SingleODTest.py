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
a=[]
for i in range(count):
    a.append(od.measure(151))
avr = sum(a)/count
b = 0
for i in a:
    b += (i-avr)**2
print((b/count)**0.5)
print(avr)

a=[]
for i in range(count):
    a.append(od.measure(255))
avr = sum(a)/count
b = 0
for i in a:
    b += (i-avr)**2
print((b/count)**0.5)
print(avr)