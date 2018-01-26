clc; clear all; close all;
rosinit;
% sub = rossubscriber('/num_pub');
% msg1 = receive(sub,10);
% pub = rospublisher('/num_sub','std_msgs/Float64');
% msg2 = rosmessage(pub);
% msg2.Data = msg1.Data + 5;
% send(pub,msg2);
% pause(10)
% rosshutdown;

% handover_package = fullfile(fileparts(which('rosgenmsg')), 'examples', 'packages');
% userFolder = 'c:\MATLAB\custom_msgs';
% copyfile(handover_package, userFolder)
% folderpath = userFolder;
% folderpath = fullfile('~/ros_ws','src');
% rosgenmsg(folderpath)

sub = rossubscriber('/skeleton_data');
msg1 = receive(sub,10);
disp(msg1);
rosshutdown;