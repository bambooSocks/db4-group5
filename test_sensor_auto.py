from od_sensor.py import ODSensor

od = ODSensor()

for i in range(256):
    print(od.measure(i))

