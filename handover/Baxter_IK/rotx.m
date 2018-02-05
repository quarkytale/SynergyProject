function R = rotx(x)
R = zeros(4,4);
R(1, 1) = 1;
R(2, 2) = cos(x);
R(2, 3) = -sin(x);
R(3, 2) = sin(x);
R(3, 3) = cos(x);
R(4, 4) = 1;
end