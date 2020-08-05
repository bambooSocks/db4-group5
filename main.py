import stepper
from machine import Pin

st = stepper.Stepper(Pin(33, Pin.OUT), Pin(27, Pin.OUT))


while (1):
    print("test")
    st.steps(-1000)