#!/usr/bin/env python
import sys
import rospy
import numpy as np
import baxter_interface
import scipy.io as sio
from tracker import Tracker

class Saver:

    def __init__(self):

        # Initialize
        self.i = 0
        self.demo_baxter_joints = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])  #Single demonstration
        self.demo_human_wrist = np.matrix([0.0, 0.0, 0.0])
        self.ht = Tracker()

        # Start Recording
        text = raw_input("Start recording demo? (Y/n)")
        if text  == 'n':
            print "No demo recorded"
        else:
            self.rec()


    def rec(self):
        while True:
            try:
                baxrarm_data = self.ht.baxter_to_record()
                self.demo_baxter_joints = np.concatenate((self.demo_baxter_joints, [baxrarm_data]), axis=0)

                h = self.ht.human_to_record()
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
            self.demo_baxter_joints = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
            self.demo_human_wrist = np.matrix([0.0, 0.0, 0.0])
            self.rec()

        sio.savemat('src/handover/promp/Data/demo_baxter.mat',{'baxter_demo_data':self.ndemos_baxter_joints})
        sio.savemat('src/handover/promp/Data/demo_human.mat',{'human_demo_data':self.ndemos_human_wrist})

def main(args):
    rospy.init_node('Saver', anonymous=True, disable_signals=True)
    sav = Saver()

if __name__ == '__main__':
    main(sys.argv)
