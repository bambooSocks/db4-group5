from machine import DAC, Pin, ADC
from time import sleep

class ODSensor:
    # frequency and pins may need to be changed
    def __init__(self,LEDPin, sensorPin): #25,39.   26,36.
        self.DAC_MAX = 255
        self.DAC_Vmax = 3.15
        self.DAC_Vmin = 0.09

        self.led = DAC(Pin(25), bits=8) 
        self.sensor = ADC(Pin(39)) #Green
        #self.sensor.atten(ADC.ATTN_11DB)
        self.sensor.width(ADC.WIDTH_10BIT)

    # return a single measurement
    def measure(self, intensity):
        self.led.write(intensity)
        sleep(0.01)
        data = []
        
        #get 120 measurements
        for j in range(120):
            data.append(self.sensor.read())

        data.sort() #sort data increasing
        sum_middle = sum(data[30:90]) #find sum of middle numbers
        avg = sum_middle / 60 #find average of middle numbers
        
        return avg