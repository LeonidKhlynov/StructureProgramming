a = []
n = int(input("Enter N: "))
b = 0
for i in range(0,n):
    a.append(int(input("Enter number: ")))
for i in range(1,n):
    if ((a[i]>0)and(a[i-1]>0)or((a[i]<0)and(a[i-1]<0))):
        b = b+1
if b>=0:
    print("Yes")
else:
    print("No")
for i in range(1,n):
    if ((a[i]>0)and(a[i-1]>0)or((a[i]<0)and(a[i-1]<0))):
        print("Success: [", a[i-1],"]; [",a[i],"]")








