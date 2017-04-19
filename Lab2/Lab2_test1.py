print('Task 1')
a = int(input('Enter a: '))
sum = a
for i in range(0,4):
    a = a//10
if (a==0)and(sum!=4999):
    print(sum,' is Success')
else:
    print(sum,'is not Success')