#!/usr/bin/env python
import roslib
#roslib.load_manifest('promp_test')
import rospy
import sys, time, os
import numpy as np
import baxter_interface
import scipy.io as sio
from human_tracker import HumanTracker

class Saver:

    def __init__(self):

    	# Initialize
    	self.i = 0
    	self.demo_baxter_joints = np.matrix([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])  #Single demonstration
    	self.demo_human_wrist = np.matrix([0.0, 0.0, 0.0])
    	self.ht = HumanTracker()

    	# Start Recording
    	text = raw_input("Start recording demo? (Y/n)")
    	if text  == 'n':
    		print "No demo recorded"
    	else:
    		self.rec()


    def rec(self):
    	while True:
    		try:
    			limb = baxter_interface.Limb('right')
    			baxarm_angles = limb.joint_angles()
    			b = np.matrix([baxarm_angles['right_s0'], baxarm_angles['right_s1'], baxarm_angles['right_e0'], baxarm_angles['right_e1'], baxarm_angles['right_w0'], baxarm_angles['right_w1'], baxarm_angles['right_w2']])
    			self.demo_baxter_joints = np.concatenate((self.demo_baxter_joints,b), axis=0)

    			h = self.ht.human()
    			self.demo_human_wrist = np.concatenate((self.demo_human_wrist,h), axis=0)

    		except KeyboardInterrupt:
    			self.i = self.i + 1
    			break

    	if self.i == 1:
    		self.ndemos_baxter_joints = [self.demo_baxter_joints[1:,:]]
    		self.ndemos_human_wrist = [self.demo_human_wrist[1:,:]]
    	else:
    		self.ndemos_baxter_joints.append(self.demo_baxter_joints[1:,:])
    		self.ndemos_human_wrist.append(self.demo_human_wrist[1:,:])

    	text = raw_input("\nRecord another demo? (Y/n)")
    	if text == 'n':
    		print "Only", self.i, "demo(s) recorded"
    	else:
    		self.demo_baxter_joints = np.matrix([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    		self.demo_human_wrist = np.matrix([0.0,0.0,0.0])
    		self.rec()

    	sio.savemat('src/promp_test/promp/Data/demo_baxter.mat',{'baxter_demo_data':self.ndemos_baxter_joints})
    	sio.savemat('src/promp_test/promp/Data/demo_human.mat',{'human_demo_data':self.ndemos_human_wrist})

def main(args):
    rospy.init_node('Saver', anonymous=True, disable_signals=True)
    sav = Saver()

if __name__ == '__main__':
    main(sys.argv)
