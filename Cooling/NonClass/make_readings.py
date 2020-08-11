from temp_control import T_control
t_control = T_control(14,32,12,34)
import utime

while True:
    f = open("data.txt","a")
    f.write(str(t_control.thermometer.read()))
    print(t_control.thermometer.read())
    f.write(" ")
    f.close()
    utime.sleep(10)