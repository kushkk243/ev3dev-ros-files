#!/usr/bin/env python
from ev3dev.ev3 import *
import rospy
from std_msgs.msg import String


rospy.init_node("ev3_node")
pub = rospy.Publisher('ev3',String,queue_size=10)
s = Sensor(address='in4',driver_name='lego-ev3-color')
#if s.connected:
assert s.connected
rate = rospy.Rate(10)
s.mode='COL-AMBIENT'
while not rospy.is_shutdown():
	msg = String()
	msg.data = str(s.value(0))
	pub.publish(msg)
	rospy.loginfo(msg.data)
	#pub.publish(msg)
	rate.sleep()
       # print(s.value(0))


