% Nama : Eko Saputra
% NIM : 201420001
% Kelas : IF4A

clc
clear
x0 = input("Masukan x0 = ");
y0 = input("Masukan y0 = ");
x1 = input("Masukan x1 = ");
y1 = input("Masukan y1 = ");

dx = x1-x0;
dy = y1-y0;

if (abs(dx)>abs(dy))
    steps = abs(dx);
else
    steps = abs(dy);
end
xinc = (dx/steps);
yinc = (dy/steps);

x(1) = x0; 
y(1) = y0;

for i = 1:steps
    x(i+1) = x(i)+xinc;
    y(i+1) = y(i)+yinc;
end
plot (round(x), round(y), 'rs');
grid on, hold on
plot(x, y, 'b');
legend('DDA points', 'Actual Point');
xlabel('x');
xlabel('y');
title('Algoritma Digital Deferential line ');