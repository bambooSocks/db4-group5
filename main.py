from mqtt import MQTT
from temp_control import T_control
from od_sensor import ODSensor
from time import sleep

if __name__ == "__main__":

    # class declarations
    broker = MQTT("iPhone", "qqwweerr")
    t_control = T_control(14,32,12,34)
    od = ODSensor()

    def subCB(topic, msg):
        if topic == "PID_P":
            print("P param for PID is", msg)
        elif topic == "PID_I":
            print("I param for PID is", msg)
        elif topic == "PID_D":
            print("D param for PID is", msg)
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
        broker.publish("temp", t_control.read())
        sleep(10)

