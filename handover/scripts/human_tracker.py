#!/usr/bin/env python
import roslib
#roslib.load_manifest('promp_test')
import rospy
import sys, time, os
import numpy as np
from kinect_data.msg import skeleton

class HumanTracker:

    def __init__(self):

        self.i = 0.0 #TODO for what?

        #Subscribing to the skeleton data from kinect
        self.data_sub = rospy.Subscriber("skeleton_data", skeleton, self.callback, queue_size = 10)

    def callback(self,data):
        self.data = data
        self.P_rw = np.matrix([self.data.joints[2].x, self.data.joints[2].y, self.data.joints[2].z])

    def human(self):
        return self.P_rw

def main(args):
    rospy.init_node('HumanTracker', anonymous=True)

    ht = HumanTracker() #TODO for what?

    try:
	rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
