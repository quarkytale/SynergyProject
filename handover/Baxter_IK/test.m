theta = zeros(4, 1);
min1 = -97.494 * pi / 180;
max1 = 97.494 * pi/180;
min2 = -123 * pi / 180;
max2 = 60 * pi/180;
min3 = -174.987 * pi / 180;
max3 = 174.987 * pi/180;
min4 = 0 * pi / 180;
max4 = 150 * pi/180;
theta(1) = rand * (max1 - min1) + min1;
theta(2) = rand * (max2 - min2) + min2;
theta(3) = rand * (max3 - min3) + min3;
theta(4) = rand * (max4 - min4) + min4;
[Pe, Pw] = FK_baxter(theta);
theta_return = IK_baxter(Pw, Pe);
theta - theta_return