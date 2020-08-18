import ssd1306
from machine import I2C, Pin
from temp_control import T_control

t_control = T_control(14,32,12,34)
i2c = I2C(scl=Pin(22), sda=Pin(23), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
oled.fill(0)
oled.text("Temperature", 0, 0) # x, y, column
oled.text(str(t_control.thermometer.read()), 10, 10)
oled.show()
