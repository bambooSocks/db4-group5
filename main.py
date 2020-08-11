from pump import VariablePump
from pump import PrecisionPump
from machine import Pin
import time

p = VariablePump(Pin(12, Pin.OUT))
p.startMotor()
p.setSpeed(1)

# pp = PrecisionPump(Pin(33, Pin.OUT), Pin(27, Pin.OUT))
# pp.step(550000)

# 1.100.000 - 190mL
#   550.000 - 95mL

# while (1):
    # print("test")
    # for i in range(11):
    #     p.setSpeed(0.1*i)
    #     time.sleep(1)