import math
print("Test 3")
a = 1
b = float(input("Enter B: "))
x = 1
z = float(input("Enter Z: "))
cos1 = (math.cos(b*(x**5)))**7
sin = math.sin(a**2)
cos2 = math.cos((x**3)+(z**5)-(a**2))
asi = math.asin(a**2)
aco = math.acos((x**7)-(a**2))
top = (cos1 - (sin + cos2))
bot = asi + aco
F = top/bot
print("F: ",F)