#!/usr/bin/env python
import rospy
import sys, time, os
import numpy as np
from kinect_data.msg import skeleton
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import PointStamped
from baxter_pykdl import baxter_kinematics

class MoveTrina:
    
    def __init__(self):

        self.goal_pub = rospy.Publisher("/goal_location", PointStamped, queue_size=1)

        self.limb = baxter_interface.Limb('right')
        self.init_angles = self.limb.joint_angles()

        self.kin = baxter_kinematics('right')

        self.angles = np.array(np.zeros(7))

        self.promp_sub = rospy.Subscriber("/promp_data", Float64MultiArray, self.callback1, queue_size = 1)
        self.otp_sub = rospy.Subscriber("/otp_estimate", PointStamped, self.callback2, queue_size=1)

    def callback1(self, data):
        self.promp = data
        for i in range(len(self.init_angles)):
            self.angles[i] = promp.data[i*99]
    
        self.angles = self.changeByAngles(self.angles, self.init_angles)
        self.promp_goal = self.kin.forward_position_kinematics(self.angles)

        self.promp_goal_trina = np.array([self.promp_goal[0], self.promp_goal[1], self.promp_goal[2] + 87.5])

        #return self.promp_goal

    def callback2(self, data):
        self.otp = data
        self.w = self.otp.header.stamp.nsecs
        self.otp_goal_trina = np.array([self.otp.point.z + 0.2, self.otp.point.x, self.otp.point.y + 1.365])

        if self.w < 0.75:
            self.goal_location = (self.w*self.promp_goal_trina) + ((1-self.w)*self.otp_goal_trina)
        else:
            self.goal_location = self.otp_goal

        self.goal_pub.publish(self.goal_location)

        self.move(self.goal_location)

    def changeByAngles(self,change_angles, angles):
        angles['right_s0']=change_angles[0]
        angles['right_s1']=change_angles[1]

        angles['right_e0']=change_angles[2]
        angles['right_e1']=change_angles[3]

        angles['right_w0']=change_angles[4]
        angles['right_w1']=change_angles[5]
        angles['right_w2']=change_angles[6]

        return angles

    def move(self, position):
        goal_angles = self.kin.inverse_kinematics(position, self.promp_goal[3:8])
        self.limb.set_joint_positions(goal_angles)

def main(args):  
    rospy.init_node('MoveTrina', anonymous=True)
    mt = MoveTrina()   

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")


if __name__ == '__main__':
    main(sys.argv)