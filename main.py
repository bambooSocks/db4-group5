from mqtt import MQTT
from temp_control import T_control
from od_sensor import ODSensor
from time import sleep
from display import Display

if __name__ == "__main__":

    # class declarations
    broker = MQTT("Asger","1234567890") 
    t_control = T_control(14,32,12,34)
    t_control.startPID()
    od = ODSensor()
    disp = Display(22,23)

    def subCB(topic, msg):
        topic = str(topic)
        
        if "PID_P" in topic:
            t_control.pid.Kp = float(msg)
        elif "PID_I_SetValue" in topic:
            t_control.pid.history = float(msg) / t_control.pid.Ki    
        elif "PID_I" in topic:
            t_control.pid.Ki = float(msg)
            print(msg)
        elif "FAN" in topic:
            if msg.decode() == "OFF":
                t_control.cooler.fanOff()
            else:
                t_control.cooler.fanOn()
        elif "target_temp" in topic:
            t_control.pid.target = float(msg) 
        else:
            print("Unknown topic received")

    # setup subscriptions
    
    broker.setCallback(subCB)
    broker.subscribe("FAN")
    broker.subscribe("PID_P")
    broker.subscribe("PID_I")
    sleep(0.1)
    broker.subscribe("PID_I_SetValue")
    broker.subscribe("target_temp")

    # main loop
    print("reached main loop")
    while True:
        # all repeating actions
        broker.publish("exp1.temperature",t_control.thermometer.read()) #testing
        disp.write("temperature: " + str(int(t_control.thermometer.read())),0,0)
        disp.write("Algae: " + "derp/mL",1,0)
        disp.plot((t_control.thermometer.read()-15)*6)
        broker.publish("exp1.P_value",t_control.pid.P_value) #testing
        broker.publish("exp1.I_value",t_control.pid.I_value) #testing
        sleep(10)

