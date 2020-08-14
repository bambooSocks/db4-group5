from mqtt import MQTT
from temp_control import T_control
from od_sensor import ODSensor
from time import sleep

if __name__ == "__main__":

    # class declarations
    broker = MQTT("Asger","1234567890") 
    t_control = T_control(14,32,12,34)
    t_control.startPID()
    od = ODSensor()

    def subCB(topic, msg):
        if topic == "PID_P":
            print("P param for PID is", msg)
        elif topic == "PID_I":
            print("I param for PID is", msg)
        elif topic == "PID_D":
            print("D param for PID is", msg)
        elif topic == "FAN":
            print("Fan is", msg)
        else:
            print("Unknown topic received")

    # setup subscriptions
    broker.setCallback(subCB)
    broker.subscribe("PID_P")
    broker.subscribe("PID_I")
    broker.subscribe("PID_D")

    # main loop
    while True:
        # all repeating actions
        broker.publish("exp1.temperature",t_control.thermometer.read()) #testing
        broker.publish("exp1.P_value",t_control.pid.P_value) #testing
        broker.publish("exp1.I_value",t_control.pid.I_value) #testing
        sleep(10)

