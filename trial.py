from ev3dev.ev3 import *
import time

ml = LargeMotor('outA')
mr = LargeMotor('outB')

ml.run_forever()
mr.run_forever()

time.sleep(10)
ml.stop()
mr.stop()
