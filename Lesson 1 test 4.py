print("Enter 4 numbers")
a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = float(input("Enter number C: "))
d = float(input("Enter number D: "))
for i in range (a,b):
	if (i % d == c):
		print("Number: ", i)