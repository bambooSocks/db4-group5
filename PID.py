class Pid:
    """
    PID control
    Stores a history
    returns a float when updated
    intented to go between 0 and 100
    """

    def __init__(self, target, P, I, D, memory):

        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.memory = memory
        self.I_value = 0
        self.P_value = 0
        self.D_value = 0
        self.history = collections.deque(maxlen=self.memory)
        for i in range(self.memory):
            self.history.append(0)
        
        self.target=target

        self.output = 0

        #self.last_update_time = pyb.millis()


    def update(self,reading):
        
        self.history.append(reading)

        self.P_value = self.Kp * (self.target-self.history[-1]) #Latest reading
        
        self.D_value = self.Kd * (self.history[-1]-self.history[-2])
        
        self.I_value = 0
        for i in range(self.memory):
            self.I_value += (self.target-self.history[i]) * self.Ki
            
    
        self.output = self.P_value + self.I_value - self.D_value
        
        #self.last_update_time=pyb.millis()
        return(self.output)