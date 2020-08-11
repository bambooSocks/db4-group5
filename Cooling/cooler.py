class Cooler:

    def __init__(self, fan_pin, peltier_pin):
        self.fan = fan_pin
        self.peltier = peltier_pin

    def fanOn(self):
        self.fan.value(1) #was inversed before, fixed now

    def fanOff(self):
        self.fan.value(0)

    def coolerLow(self):
        self.peltier.value(1) #was inversed before, fixed now (probably)

    def coolerHigh(self):
        self.peltier.value(0)