# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:47:28 2020

@author: Arepy
"""
import utime
from cooler import Cooler
from PID import Pid
#from pump import VariablePump
from pump import PWMPump
from read_temp_class import Thermometer
from machine import Pin
import _thread



class T_control:    
    def __init__(self, fan_pin, peltier_pin, step_pin,thermometer_pin):
        self.cooler = Cooler(Pin(fan_pin,Pin.OUT), Pin(peltier_pin,Pin.OUT))
        self.cooler.fanOn()
        self.cooler.coolerHigh()
        
        
        self.pid = Pid(17,1,0.02,0,0.995)  #(temperature, P, I, D, memoryFactor)
        self.thermometer = Thermometer(thermometer_pin)
        self.pump = PWMPump(Pin(step_pin,Pin.OUT))
        for i in range(10):
            self.pump.pwm.freq(i*1500)
            utime.sleep(0.1)
        self.pump.pwm.freq(15000)
        #self.pump = VariablePump(Pin(step_pin,Pin.OUT))
        #self.pump.setSpeed(0.90)
        #self.pump.startMotor()
        
        
        
    def call(self):
        self.t=utime.time()
        read=-self.pid.update(self.thermometer.read())
        if read > 2:
            self.cooler.coolerHigh()
            self.pump.pwm.freq(10000)
        elif read >= 1:
            self.cooler.coolerLow()
            self.pump.pwm.freq(10000)
        elif read >= -1:
            self.cooler.coolerLow()
            self.pump.pwm.freq(6666+int(3333*read))
        else:
            self.cooler.coolerLow()
            self.pump.pwm.freq(200)
    
    def __loop(self):
        while self.isRunning:
            self.call()
            utime.sleep(10)
            

    def startPID(self):
        self.isRunning = True
        _thread.start_new_thread(self.__loop, ())    
        
    def stopPID(self):
        self.isRunning = False