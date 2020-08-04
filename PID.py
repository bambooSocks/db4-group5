# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Pid:
    """
    Discrete PID control
    """

    def __init__(self, target, P=3.0, I=0.01, D=0.0):

        self.Kp=P
        self.Ki=I
        self.Kd=D

        self.I_value = 0
        self.P_value = 0
        self.D_value = 0
        self.history = collections.deque(maxlen=20)
        for i in range(20):
            self.history.append(0)
        
        self.target=target

        self.output = 0

        #self.last_update_time = pyb.millis()


    def update(self,reading):
        
        self.history.append(reading)

        self.P_value = self.Kp * (self.target-self.history[-1]) #Latest reading
        
        self.D_value = self.Kd * (self.history[-1]-self.history[-2])
        
        self.I_value = 0
        for i in range(20):
            self.I_value += (self.target-self.history[i]) * self.Ki
            
    
        self.output = self.P_value + self.I_value - self.D_value
        
        #self.last_update_time=pyb.millis()
        return(self.output)