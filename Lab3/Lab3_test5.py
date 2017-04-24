print('Task 5')
print()
n = int(input('Enter N: '))
prv1 = 1
prv2 = 0
sum = 0
i = 1
while i < n:
    sum = prv1 + prv2
    prv1 = prv2
    prv2 = sum
    print(i,": ",sum)
    i += 1








