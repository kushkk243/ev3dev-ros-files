from ev3dev.ev3 import *

s = Sensor(address='in4',driver_name='lego-ev3-color')
assert s.connected
s.mode='COL-AMBIENT'
while True:
	print(s.value(0))
