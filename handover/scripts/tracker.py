#!/usr/bin/env python
import sys
import rospy
import numpy as np
from handover.msg import skeleton
import baxter_interface
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Float64MultiArray

class Tracker:

    def __init__(self):

        #Publish human wrist data
        self.wrist_pub = rospy.Publisher("wrist_data", PointStamped, queue_size = 10)  
        #Publish baxter joint angles
        self.baxter_pub = rospy.Publisher("baxter_joints", Float64MultiArray, queue_size = 10)      

        #Subscribing to the skeleton data from kinect
        self.data_sub = rospy.Subscriber("skeleton_data", skeleton, self.callback, queue_size = 10)

    def callback(self,data):
        self.data = data

        self.h = PointStamped()
        self.h.header.stamp.secs = float(self.data.joints[2].stamp)
        self.h.point.x = self.data.joints[2].x
        self.h.point.y = self.data.joints[2].y
        self.h.point.z = self.data.joints[2].z

        limb = baxter_interface.Limb('right')
        baxarm_angles = limb.joint_angles()

        self.b = Float64MultiArray()
        self.b.data = np.array([baxarm_angles['right_s0'], baxarm_angles['right_s1'], baxarm_angles['right_e0'], baxarm_angles['right_e1'], baxarm_angles['right_w0'], baxarm_angles['right_w1'], baxarm_angles['right_w2']])

        
        self.wrist_pub.publish(self.h)
        self.baxter_pub.publish(self.b)

    def baxter_to_record(self):
        return self.b.data      

    def human_to_record(self):
        self.P_rw = np.matrix([self.data.joints[2].x, self.data.joints[2].y, self.data.joints[2].z])
        return self.P_rw


def main(args):

    rospy.init_node('Tracker', anonymous=True, disable_signals=True)
    trac = Tracker()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
