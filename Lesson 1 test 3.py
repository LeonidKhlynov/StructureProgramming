print("Enter 3 parts: ")
a = int(input("Enter 1 part: "))
b = int(input("Enter 2 part: "))
c = int(input("Enter 3 part: "))
if (a+b>c):
    if (a+c>b):
        if (b+c>a):
            print("Correct")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")