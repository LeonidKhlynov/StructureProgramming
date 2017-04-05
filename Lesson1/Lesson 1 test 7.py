x = float(input("Enter x: "))
y = float(input("Enter y: "))
i = 1
while x<y:
    lo = x*10/100
    x = x + lo
    lo = 0
    i = i + 1
print("Day: ", i)
print("Km: ", x)
