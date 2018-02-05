% this function is used for solving Baxter right arm IK given Pw, Pe.
function theta = IK_baxter(Pw, Pe)
% Pw is the distance from the shoulder(s0) to endeffector(end of w2), Pe is the distance
% from shoulder(s0) to elbow(e1).
% theta1 (s0) 97.494 to -97.494
% theta2 (s1) 60 to -123
% theta3 (e0) 174.987 to -174.987
% theta4 (e1) 150 to -2.864
% theta5 (w0) 175.25 to -175.25
% theta6 (w1) 120 to -90
% theta7 (w2) 175.25 to -175.25
theta = zeros(4,1);
l1 = 0.069;
l2 = 0.37082;
l3 = 0.37442;
l4 = 0.229525;
% Pe depends on theta1 and theta2 only
sin2 = -Pe(3)/l2;
cos2 = (norm(Pe)^2 - l1^2 - l2^2)/(2 * l1 * l2);
theta(2) = atan2(sin2, cos2);
sin1 = Pe(1)/(l1 + cos(theta(2)) * l2);
cos1 = -Pe(2)/(l1 + cos(theta(2)) * l2);
theta(1) = atan2(sin1, cos1);
T01 = rotz(theta(1)) * transy(-l1);
T12 = rotx(theta(2));
T01_inver = inverT(T01);
T12_inver = inverT(T12);
Pw_2 = T12_inver * T01_inver * [Pw; 1]; % Pw in frame 2
p1 = Pw_2(1);
p2 = Pw_2(2);
p3 = Pw_2(3);
cos4 = -(p2 + l2)/l3;
sin4 = sqrt((p1^2 + p3^2)/l3^2);
theta(4) = atan2(sin4, cos4);
sin3 = -p1/sin(theta(4))/l3;
cos3 = -p3/sin(theta(4))/l3;
theta(3) = atan2(sin3, cos3);
end