from temp_control import T_control
t_control = T_control(14,32,12,34)
import utime
from mqtt import MQTT

MQTT1 = MQTT("Asger","1234567890")

while True:
    t_control.call()
    
    MQTT1.publish("exp1.temperature",t_control.thermometer.read())
    MQTT1.publish("exp1.P_value",t_control.pid.P_value)
    MQTT1.publish("exp1.I_value",t_control.pid.I_value)
    
    utime.sleep(10)
    