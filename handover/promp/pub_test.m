clc; close all;
rosinit;
pub = rospublisher('/promp_data', 'std_msgs/Float64MultiArray');
M = [];
for i = 4:10
    M = [M, kf1(i).q_mean];
end
msg = rosmessage(pub);
msg.Data = M;
send(pub,msg);
pause(1);
rosshutdown