import math
print('Task 6')
print()
r1 = float(input('Enter r1: '))
r2 = float(input('Enter r2: '))
r3 = float(input('Enter r3: '))
mxq = float
mnf = float
E = 3
e = 1
e0 = 8.85*(10**-12)
q1 = E/(4*math.pi*e0*e*(r1**2))
q2 = E/(4*math.pi*e0*e*(r2**2))
q3 = E/(4*math.pi*e0*e*(r3**2))
f1 = E*r1
f2 = E*r2
f3 = E*r3
if (q1>q2)and(q1>q3):
    mxq = q1
else:
    if (q2>q1)and(q2>q3):
        mxq = q2
    else:
        mxq = q3
if (f1<f2)and(f1<f3):
    mnf = f1
else:
    if (f2<f1)and(f2<f3):
        mnf = f2
    else:
        mnf = f3
print()
print('Max q: ',mxq)
print('Min F: ',mnf)

