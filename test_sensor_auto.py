import machine
import time
from machine import DAC

DAC_MAX = 255
DAC_Vmax = 3.15
DAC_Vmin = 0.09
dac = DAC(machine.Pin(25), bits=8)

adc = machine.ADC(machine.Pin(39)) #create adc object
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP) #create button object

for i in range(256):
    dac.write(i)
    time.sleep(0.01)
    data = []
    
    #get 120 measurements
    for j in range(120):
        data.append(adc.read())

    data.sort() #sort data increasing
    
    sum_middle = sum(data[30:90]) #find sum of middle numbers
    
    avg = sum_middle / 60 #find average of middle numbers
    
    print(avg)

