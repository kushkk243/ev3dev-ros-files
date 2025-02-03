from time import sleep
#import rospy
#from std_msgs.msg import String
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
td=MoveTank(OUTPUT_A,OUTPUT_B)

if __name__=="__main__":
	#rospy.init_node("new_test_node")
	#pub = rospy.Publisher("node1", String, queue_size=10)
	#rate = rospy.Rate(1)
	#while not rospy.is_shutdown():
	td.on_for_rotations(SpeedPercent(50),SpeedPercent(50),10)
	#	msg = String()
	#	msg.data="Done"
	#	pub.publish(msg)
	#	rate.sleep()
