"""Micropython module for stepper motor driven by Easy Driver."""
from machine import Pin
from time import sleep_us


class Stepper:
    """Class for stepper motor driven by Easy Driver."""

    def __init__(self, step_pin, dir_pin):
        """Initialise stepper."""
        self.stp = step_pin
        self.dir = dir_pin

        self.stp.init(Pin.OUT)

        if self.dir is not None:
            self.dir.init(Pin.OUT)

        self.step_time = 20  # us
        self.steps_per_rev = 1600
        self.current_position = 0

    def steps(self, step_count):
        """Rotate stepper for given steps."""
        if self.dir is not None:
            self.dir.value(0 if step_count > 0 else 1)
        for i in range(abs(step_count)):
            self.step()
        self.current_position += step_count

    def step(self):
        self.stp.value(1)
        sleep_us(1)
        self.stp.value(0)
        sleep_us(int(self.step_time))

    def rel_angle(self, angle):
        """Rotate stepper for given relative angle."""
        steps = int(angle / 360 * self.steps_per_rev)
        self.steps(steps)

    def abs_angle(self, angle):
        """Rotate stepper for given absolute angle since last power on."""
        steps = int(angle / 360 * self.steps_per_rev)
        steps -= self.current_position % self.steps_per_rev
        self.steps(steps)

    def revolution(self, rev_count):
        """Perform given number of full revolutions."""
        self.steps(rev_count * self.steps_per_rev)

    def set_step_time(self, us):
        """Set time in microseconds between each step."""
        if us < 20:  # 20 us is the shortest possible for esp8266
            self.step_time = 20
        else:
            self.step_time = us