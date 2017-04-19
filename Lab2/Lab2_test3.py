import math
print('Task 4')
print()
x = float(input('Enter x: '))
y = float(input('Enter y: '))
if ((x<=2)and(x>=-2))and(y>=(x**2)-2)and(y<=abs(x)):
    print('Success')
else:
    print('Error')