function [Pe, Pw] = FK_baxter(theta)
l1 = 0.069;
l2 = 0.37082;
l3 = 0.37442;
T01 = rotz(theta(1)) * transy(-l1);
T12 = rotx(theta(2));
T23 = roty(theta(3)) * transy(-l2);
T34 = rotx(theta(4));
Pe_1 = T01 * T12 * [0; -l2; 0; 1];
Pw_1 = T01 * T12 * T23 * T34 * [0; -l3; 0; 1];
Pe = Pe_1(1:3);
Pw = Pw_1(1:3);
end