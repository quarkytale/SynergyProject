clc; clear all; close all;
rosinit;
sub = rossubscriber('/num_pub');
msg1 = receive(sub,10);
pub = rospublisher('/num_sub','std_msgs/Float64');
msg2 = rosmessage(pub);
msg2.Data = msg1.Data + 5;
send(pub,msg2);
pause(10)
rosshutdown;