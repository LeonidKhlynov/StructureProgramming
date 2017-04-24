print('Task 1')
print()
sum = 0
for i in range(1,1000):
    for j in range (1,i+1):
        if (i%j==0):
            sum = sum + 1
    if sum==5:
        print("Sum: ",i)
    sum = 0



