import math
print("Test 2")
k = float(input("Enter k: "))
y = float(input("Enter y: "))
k = 2 * k + 4.3
lan = math.log(k)
ex = (math.e**(k+y)) + math.sqrt(y)
U = lan/ex
print("U: ",U)