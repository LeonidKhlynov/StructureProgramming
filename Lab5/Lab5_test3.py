def inp(a,b):
    for i in range(0,b):
        a.append(int(input('Enter double: ')))

print('Task 3')
print()
n = int(input("Enter number of parameters: "))
a = []
i = n-1
inp(a,n)
while i != 0:
    a[i],a[i-1] = a[i-1], a[i]
    i = i - 1
print(a)



