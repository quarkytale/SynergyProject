#!/usr/bin/env python
import roslib
#roslib.load_manifest('promp_test')
import rospy
import sys, time, os
import numpy as np
from kinect_data.msg import skeleton
import baxter_interface
import scipy.io as sio
from handover.msg import pos

class HumanTracker:

    def __init__(self):

        self.i = 0.0 #TODO for what?

        #Subscribing to the skeleton data from kinect
        self.data_sub = rospy.Subscriber("skeleton_data", skeleton, self.callback, queue_size = 10)
        self.h_pub = rospy.Publisher("human_wrist", pos, queue_size=10)

    def callback(self,data):
        self.data = data
        self.P_rw = np.matrix([self.data.joints[2].x, self.data.joints[2].y, self.data.joints[2].z])
        self.h = ([self.data.joints[2].x, self.data.joints[2].y, self.data.joints[2].z, float(self.data.joints[2].stamp)])
        rospy.loginfo(self.h)
        self.h_pub.publish(self.h)


    def human(self):
        return self.P_rw

def main(args):

    rospy.init_node('HumanTracker', anonymous=True)

    ht = HumanTracker()

    try:
	rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
