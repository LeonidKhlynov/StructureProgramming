import math
print("Test 4")
a = float(input("Enter a > 0: "))
b = float(input("Enter b > 0: "))
if (a <= 0 )or(b <= 0):
    print("Error. Not correct number ")
else:
    s = a * b
    print("MidlGeom: ",math.sqrt(s))