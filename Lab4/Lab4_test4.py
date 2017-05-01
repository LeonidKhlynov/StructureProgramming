print("Task 4")
print()
s = input("Enter s: ")
a = s.split(' ')
sum = 0
for i in range(len(a)):
    if sum==1:
        print('Only 1: ',test)
    test = a[i]
    sum = 0
    for j in range(len(a)):
        if test == a[j]:
            sum += 1



