print("Enter 3 numbers")
a = int (input("Enter number: "))
b = int (input("Enter number: "))
c = int (input("Enter number: "))
if (a>b):
    if (a>c):
        print(a, "is the biggest number")
    else:
        print(c, "is the biggest number")
else:
    if (b>c):
        print(b, "is the biggest number")
    else:
        print(c, "is the biggest number")