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
        
        
        self.pid = Pid(18,3,0.01,0,200)#temperature, P, I, D, Memory
        self.thermometer = Thermometer(thermometer_pin)
        self.pump = PWMPump(Pin(step_pin,Pin.OUT))
        self.pump.pwm.freq(15000)
        #self.pump = VariablePump(Pin(step_pin,Pin.OUT))
        #self.pump.setSpeed(0.95)
        #self.pump.startMotor()
        self.t = utime.time()
        self.intensity = 0
        
        
        
    def call(self):
        #find out how long has passed since last call
        dt = utime.time()-self.t
        self.t=utime.time()
        pid=self.pid.update(self.thermometer.read())/100
        print(pid)
        self.intensity += dt*pid
        if self.intensity >= dt:
            self.cooler.coolerLow()
            self.intensity-=dt
        else:
            self.cooler.coolerHigh()
    
        