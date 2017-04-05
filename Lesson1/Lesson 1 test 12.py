ar = input("Enter string: ")
bl = True
for i in range(0, len(ar)//2):
    if (ar[i]!= ar[len(ar) - 1 - i]):
        bl = False
if bl:
    print("Success")
else:
    print("Error")
