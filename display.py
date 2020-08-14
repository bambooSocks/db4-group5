import ssd1306
from machine import I2C, Pin
class Display:
    def __init__(self,scl_pin,sda_pin):
        
        i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)
        self.oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        self.oled.fill(0)
        self.oled.show()
        self.plotX = 0
        self.yMax = 44
    def write(self,text,line,x):
        for a in range(10):
            for b in range(128):
                self.oled.pixel(b,a+line*10,0)
        self.oled.text(text,x,line*10)
        self.oled.show()
    
    def clear(self):
        self.oled.fill(0)
        self.oled.show()
    
    def plot(self,datapoint):
        if datapoint > 44:
            datapoint = 44
        elif datapoint < 0:
            datapoint = 0
        dp = int(datapoint)
        for i in range(44):
            self.oled.pixel(self.plotX,i+20,0)
        self.oled.pixel(self.plotX,44-dp+20,1)
        self.plotX+=1
        if self.plotX >127:
            self.plotX = 0
        self.oled.show()
        