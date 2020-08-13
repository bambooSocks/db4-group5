class Pid:
    """
    PID control
    Stores a history
    returns a float when updated
    intented to go between 0 and 100
    """
    from collections import deque
    def __init__(self, target, P, I, D, memoryFactor): #Memory factor 0.99 is a halftime of 11½ min

        self.Kp=P
        self.Ki=I
        self.Kd=D
        
        self.I_value = 0
        self.P_value = 0
        self.D_value = 0
        
        self.memoryFactor = memoryFactor
        self.history = 0
        self.historyWeight = 0
        
        self.target=target

        self.output = 0
        
        self.lastDiff = 0


    def update(self,reading):
        diff = self.target - reading
        
        self.history = self.history*self.memoryFactor
        self.history += diff
        
        self.P_value = self.Kp * diff
        self.I_value = self.Ki * self.history
        self.D_value = self.Kd * (diff-self.lastDiff)
        self.output = self.P_value + self.I_value + self.D_value
        
        self.lastDiff = diff
        
        return(self.output)