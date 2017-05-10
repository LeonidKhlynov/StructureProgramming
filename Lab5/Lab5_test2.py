print('Task 2')
print()
a = []
b = []
for i in range(0,10):
    a.append(int(input('Enter number: ')))
    one = a[i]//10
    two = a[i]%10
    b.append(one - two)
print(b)

