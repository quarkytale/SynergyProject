#!/usr/bin/env python
import sys
import rospy
import time
import numpy as np
from std_msgs.msg import Float64MultiArray
import baxter_interface 

class MoveBaxter:
    
    def __init__(self):

        self.limb = baxter_interface.Limb('right')
        self.init_angles = self.limb.joint_angles()
        self.angles = np.array(np.zeros(7))

        # Initial baxter's monkey-like pose:
        # self.angles = {'right_s0': -0.27167167047229857, 'right_s1': 1.0470000139534008, 'right_w0': 0.33384006918791975, 'right_w1': -0.005184869782518753, 'right_w2': 1.2366728384114642, 'right_e0': -0.006598568301393826, 'right_e1': 0.49706985919047053}

        # Initial human-like hand position:
        # self.init_angles = {'right_s0': -0.8939273041402248, 'right_s1': 1.0227816903225997, 'right_w0': 0.0019174759848567672, 'right_w1': -0.002684466378799474, 'right_w2': 0.08015049616701286, 'right_e0': 1.0009224640952326, 'right_e1': 0.46057773156259546}

        self.num_sub = rospy.Subscriber("/promp_data", Float64MultiArray, self.callback, queue_size = 1)

    def callback(self, data):
        promp = data

        for i in range(len(self.angles)):
            self.angles[i] = promp.data[((i+1)*99)-1]

        print self.angles
    
        self.joint_angles = self.changeByAngles(self.angles, self.init_angles)

        self.move(self.limb, self.joint_angles)

    def changeByAngles(self,change_angles, angles):
        angles['right_s0']=change_angles[0]
        angles['right_s1']=change_angles[1]

        angles['right_e0']=change_angles[2]
        angles['right_e1']=change_angles[3]

        angles['right_w0']=change_angles[4]
        angles['right_w1']=change_angles[5]
        angles['right_w2']=change_angles[6]

        return angles

    def move(self,limb, angles):
        limb.set_joint_positions(angles)

def main(args):  
    rospy.init_node('MoveBaxter', anonymous=True)
    mb = MoveBaxter()   

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")


if __name__ == '__main__':
    main(sys.argv)




