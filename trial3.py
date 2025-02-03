from ev3dev.ev3 import *
import time
motorA = LargeMotor('outA')
motorB = LargeMotor('outB')

# Run the motors
motorA.run_forever(speed_sp=500)
motorB.run_forever(speed_sp=500)

time.sleep(10)
motorA.stop()
motorB.stop()
