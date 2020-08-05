from stepper import Stepper
import _thread

# used for the cooling/OD pump
class VariablePump:

    def __init__(self, step_pin):
        self.stepper = Stepper(step_pin, None)
        self.isRunning = False

        self.maxSpeedDelay = 20
        self.minSpeedDelay = 1000

    # speed is float between 0 - 1
    def setSpeed(self, speed):
        assert speed > 1 or speed < 0

        speedRange = self.minSpeedDelay - self.maxSpeedDelay
        speedDelay = self.minSpeedDelay - (speedRange * speed)
        self.stepper.set_step_time(speedDelay)

    # do not use outside of the class
    def __loop(self):
        while self.isRunning:
            self.stepper.steps(20)

    def startMotor(self):
        self.isRunning = True
        _thread.start_new_thread(__loop, ())

    def stopMotor(self):
        self.isRunning = False

# used for the feeding pump
class PrecisionPump:

    def __init__(self, step_pin, dir_pin):
        self.stepper = Stepper(step_pin, dir_pin)
        self.stepper.set_step_time(100)
        self.dir = 1

        self.stepsPerML = 7 #TODO: determine proper amount

    def feed(self, ml_amount):
        stepsToTake = ml_amount * self.stepsPerML * self.dir
        self.stepper.steps(stepsToTake)

    # just for testing
    def step(self, steps):
        self.stepper.steps(steps)

    def reverse(self):
        self.dir = 1 if self.dir == 1 else -1