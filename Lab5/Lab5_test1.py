print('Task 1')
print()
a = []
sum = 0
num = 0
for i in range(0, 12):
    a.append(float(input("Enter number: ")))
for i in range(0, 12):
    if a[i] < a[11]:
        sum = sum + a[i]
        num = num + 1
if sum > 0 and num > 0:
    print('Sum :', sum)
    print('Numbers < ', a[11],': ', num)
else:
    print('Zero parametr')

