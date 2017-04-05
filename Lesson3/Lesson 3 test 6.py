import math
print("Test 6")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
h = float(input("Enter h: "))
s1 = a * a
s2 = b * b
V = h*(s1 + math.sqrt(s1*s2) + s2)/3
print("V: ",V)