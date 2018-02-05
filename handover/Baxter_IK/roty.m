function R = roty(x)
R = zeros(4,4);
R(2, 2) = 1;
R(1, 1) = cos(x);
R(3, 1) = -sin(x);
R(1, 3) = sin(x);
R(3, 3) = cos(x);
R(4, 4) = 1;
end