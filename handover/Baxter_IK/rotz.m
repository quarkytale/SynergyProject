function R = rotz(x)
R = zeros(4,4);
R(3, 3) = 1;
R(1, 1) = cos(x);
R(1, 2) = -sin(x);
R(2, 1) = sin(x);
R(2, 2) = cos(x);
R(4, 4) = 1;
end