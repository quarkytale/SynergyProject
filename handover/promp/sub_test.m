clc; clear all; close all;
rosinit;
X = [];
w = [];
sub = rossubscriber('/wrist_data');
while 1
    msg1 = receive(sub,15);
    X = [X, msg1.Point.X];
    w = [w, msg1.Header.Seq];
    if w(end)>80
        break;
    end
end
pause(1);
rosshutdown