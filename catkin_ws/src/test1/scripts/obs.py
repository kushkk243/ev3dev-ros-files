#!/usr/bin/env python
import rospy
from ev3dev.ev3 import *
import time
from std_msgs.msg import String

rospy.init_node("ev3_node")
pub = rospy.Publisher("ev3", String, queue_size=10)
rate = rospy.Rate(10)
motorA = LargeMotor('outA')
motorB = LargeMotor('outB')
s = Sensor(address='in1',driver_name='lego-ev3-us')
assert s.connected
s.mode='US-DIST-CM'
msg = String()
# Run the motors
while not rospy.is_shutdown():
	msg.data=str(s.value(0))
	#print(s.value(0))
	pub.publish(msg)
	rospy.loginfo(msg.data)
	motorA.duty_cycle_sp=40
	motorA.run_direct()
	motorB.duty_cycle_sp=40
	motorB.run_direct()
	if s.value(0) < 200:
		motorA.stop()
		motorB.stop()
		motorB.duty_cycle_sp=40
		motorB.run_direct()
		time.sleep(5)
	#if s.value(0) < 150:
	#	break
		#motorA.stop()
		#motorB.stop()
		#motorA.run_timed(time_sp=10000,speed_sp=500)
		#motorB.stop()
	#motorA.run_forever(speed_sp=500)
	#motorB.run_forever(speed_sp=500)

motorA.stop()
motorB.stop()
