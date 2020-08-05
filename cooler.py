class Cooler:

    def __init__(self, fan_pin, peltier_pin):
        self.fan = fan_pin
        self.peltier = peltier_pin

    def fanOn(self):
        self.fan.value(0)

    def fanOff(self):
        self.fan.value(1)

    def coolerLow(self):
        self.peltier.value(0)

    def coolerHigh(self):
        self.peltier.value(1)