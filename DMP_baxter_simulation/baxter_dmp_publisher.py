import rospy
#import baxter_interface
import numpy as np
import matplotlib.pyplot as plt
from train_dmp import train_dmp
from DMP_runner import DMP_runner
#from simple_trajectories import y_cubed_trajectory
#from simple_trajectories import y_lin_trajectory
import simple_trajectories
from std_msgs.msg import String
#Name of the file
filename = []
for i in range(0,7):
    A='{}{}{}'.format('joint',i,'.xml')
    filename.append(A)

#Set no. of basis functions
n_rfs = 200

#Set the time-step
dt = 0.001


##### TRAJECTORY  FOR TRAINING ########
""" Available trajectories: ('ok')

    Linear = simple_trajectories.y_lin_trajectory(dt)
    Exponential = simple_trajectories.y_exp_trajectory(dt)
    Step = simple_trajectories.y_step_trajectory(dt)
    Baxter_s0 = simple_trajectories.bax_trajectory(dt,x) [x = 9 to x = 15 for the 7 baxter joints]
"""
X = []
for i in range(1,8):
    T = simple_trajectories.bax_trajectory(dt,i+8)
    X.append(T)
#Obtain w, c & D (in that order) from below function, and generate XML file

for i in range(0,7):
    Important_values = train_dmp(filename[i], n_rfs, X[i], dt)

#start = 0
#goal = 1
Y = []

####BELOW IS GIVEN A NEW POSITION, YOU CAN TEST THE "GOAL" AS THIS POSITION FOR THE JOINTS TO TRY IT OUT.########

#position = [0.43707952457256116, 0.030886485048354118, -0.9100930412938544,-0.049960844259059556,0.11294876661665842, -0.7784898036329784, 0.026319462646594793]
my_runner = [[]]*7
position = [0.43707952457256116, 0.030886485048354118, -0.9100930412938544,-0.049960844259059556,0.11294876661665842, -0.7784898036329784, 0.026319462646594793]
for x in range(0,7):
    start = X[x][0]
    #goal = X[x][-1]
    goal = position[x]
    my_runner[x] = DMP_runner(filename[x],start,goal)

#Default.Initial_position()
tau = 1
#for i in np.arange(0,int(tau/dt)+1):
Command_Publisher = rospy.Publisher('commands', String,queue_size=10)
rospy.init_node('commands', anonymous=True)
for i in np.arange(0,int(tau/dt)+1):
    '''Dynamic change in goal'''
    if i > 0.1*int(tau/dt):
        for i in range(7):        
            my_runner[i].setGoal(position[i],1)
    '''Dynamic change in goal'''  
    for i in range(len(my_runner)):
    	my_runner[i].step(tau,dt)
       	Y.append(my_runner[i].y)
    Y_str=','.join(str(e) for e in Y)
    Command_Publisher.publish(Y_str)
    Y = []
print('done')
"""Plot Function
time = np.arange(0,tau+dt,dt)
plt.title("2-D DMP demonstration")
plt.xlabel("Time(t)")
plt.ylabel("Position(y)")
for i in range(0,7):
	#plt.plot(X[i])
	#plt.plot(Y[i])
	#plt._show()
"""


