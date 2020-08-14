from temp_control import T_control
t_control = T_control(14,32,12,34)
t_control.startPID()
import utime
while True:
    p = open("p.txt","a")
    p.write(str(t_control.pid.P_value)+" ")
    p.close()
    
    i = open("i.txt","a")
    i.write(str(t_control.pid.I_value)+" ")
    i.close()
    
    t = open("t.txt","a")
    t.write(str(t_control.thermometer.read())+" ")
    t.close()
    utime.sleep(60)