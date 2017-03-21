a = ['0','1','2','3','4','5','6','7','8','9']
num = (input("Enter symbol: "))
b = True
ls = len(a)
for i in range(0,9):
    if (a[i]==num):
        b = True
        break
    else:
        b = False
if b:
    print("Success")
else:
    print("Error")

