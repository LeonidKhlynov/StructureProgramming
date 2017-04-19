import math
print('Task 4')
a = float(input("Enter parametr:"))
print()
Strg = (a ** 2) * math.sqrt(3/4)
rcrc = a * math.sqrt(3/6)
Scrc = math.pi * (rcrc ** 2)
if Strg >= Scrc:
    print("A) Success: Triangle Square >= Circle Square ")
else:
    print("A) Error: Triangle Square < Circle Square ")
rcrc = a * math.sqrt(3/3)
Scrc = math.pi * (rcrc ** 2)
if Scrc >= Strg:
    print("B) SuccessL: Circle Square >= Triangle Square")
else:
    print("B) Error: Circle Square < Triangle Square")
