import machine
from statistics import mean

class ODSensor:
    # frequency and pins may need to be changed
    def __init__(self, adc, led):
        self.adc = machine.ADC(machine.Pin(32))
        self.led = machine.PWM(machine.Pin(27), freq = 78000)

    # return a single measurement
    def measure(self):
        # LED duty cycle may need to be changed
        self.led.duty(31)

        data = []
        
        # get 120 measurements
        for j in range(120):
            data.append(self.adc.read())

        # sort data increasing
        data.sort()
        
        # return average of middle numbers
        return mean(data[30:90])