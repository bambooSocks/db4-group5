# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:47:28 2020

@author: Arepy
"""
import utime
import collections
from cooler import Cooler
from PID import Pid
#from pump import VariablePump
from pump import PWMPump
from read_temp_class import Thermometer
from machine import Pin

class T_control:    
    def __init__(self, fan_pin, peltier_pin, step_pin,thermometer_pin):
        self.cooler = Cooler(Pin(fan_pin,Pin.OUT), Pin(peltier_pin,Pin.OUT))
        
        self.cooler.fanOn()
        self.cooler.coolerHigh()
        
        
        self.pid = Pid(17,1,0.01,0,0.99)  #(temperature, P, I, D, memoryFactor)
        self.thermometer = Thermometer(thermometer_pin)
        self.pump = PWMPump(Pin(step_pin,Pin.OUT))
        for i in range(14):
            self.pump.pwm.freq(500+i*1000)
            utime.sleep(0.1)
        self.pump.pwm.freq(15000)
        #self.pump = VariablePump(Pin(step_pin,Pin.OUT))
        #self.pump.setSpeed(0.90)
        #self.pump.startMotor()
        
        
        
    def call(self):
        self.t=utime.time()
        read=-self.pid.update(self.thermometer.read())
        print(read)
        if read > 2:
            self.cooler.coolerHigh()
            self.pump.pwm.freq(15000)
        elif read >= 1:
            self.cooler.coolerLow()
            self.pump.pwm.freq(15000)
        elif read >= -2:
            self.cooler.coolerLow()
            self.pump.pwm.freq(10000+4750*read)
        else:
            self.cooler.coolerLow()
            self.pump.pwm.freq(500)
    
        