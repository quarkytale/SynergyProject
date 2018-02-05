%% Train the ProMP

clear; close all; clc; dbstop if error;
addpath('func/');
addpath('func_plot/');
addpath('Data/');       % data set created previously. Just load it.

% get traj distribution
dt       = 0.01;
[data]   = loadData(dt);

% plot individual joints
[data, h] = plot_nStates(data);

% put data in the ClassSystem-like formatclear
data_ias = format_ias_data(data);

%[h] = plot2DwrapA(h, data);
 
% create the ProMP (ProMP) here
ProMP = regression_pmp(data_ias, 30, 'GaussianFeatures');

%% Online ProMP

% create a parameter structure that is useful for several functions
param.nTraj = data(1).nSize;
param.nTotalJoints = ProMP.nJoints;
param.observedJointPos = [1 2 3];
param.observedJointVel = [ ];
 
dataSet = 1;
 
% in KF context this says how much noise there is in the observation
stdev = 0.005;
 
% create observation object here
obs = Observation(dataSet , stdev, param);
 
rosinit;
sub = rossubscriber('/wrist_data');
pub = rospublisher('/promp_data', 'std_msgs/Float64MultiArray');
msg2 = rosmessage(pub);

otp_weight = [];

while 1
    % receive the human data
    msg1 = receive(sub,1);
    
    
    if msg1.Header.Stamp.Nsec < 100
        % point data
        point = [msg1.Point.X, msg1.Point.Y, msg1.Point.Z];
        
        otp_weight = [otp_weight, [msg1.Header.Stamp.Nsec; point']];
        
        % define the points in the data set to be measured, and update the object
        observed_data_index = 100 - msg1.Header.Stamp.Nsec;
        obs.measuredIndexes(observed_data_index, data, point);

        [kf1] = mainloop(h, ProMP, param, obs);
        
        M = [];
        for i = 4:10
            M = [M, kf1(i).q_mean];
        end
        
        msg2.Data = M;
        send(pub,msg2);
        
        if msg1.Header.Stamp.Nsec < 35
            break;
        end
        
    end
    
end

rosshutdown
 
%% Offline ProMP
% create a parameter structure that is useful for several functions
param.nTraj = data(1).nSize;
param.nTotalJoints = ProMP.nJoints;
param.observedJointPos = [1 2 3];
param.observedJointVel = [ ];

dataSet = 3;

% in KF context this says how much noise there is in the observation
stdev = 0.005; 

% create observation object here
obs = Observation2(dataSet , stdev, param);            
              
% define the points in the data set to be measured, and update the object
observed_data_index = 40;              
obs.measuredIndexes(observed_data_index, data);
            
%plot test data
for j=1:param.nTotalJoints
    figure(h(j).q); grid off;
    plot(data(j).q(obs.set, :), SBLACK(2));  
    figure(h(j).qdot); grid off;
    plot(data(j).qdot(obs.set, :), SBLACK(2));  
end

[kf1] = mainloop2(h, ProMP, param, obs);


 
 
 
 
 
 
 
 
 

