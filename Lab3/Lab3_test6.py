print('Task 6')
print()
n = int(input('Enter n: '))
x = int(input("Enter x: "))
sum = 0
for i in range(1,n):
    sum = sum + ((-1)**i)*((x+1)**(i*2))/i
    print(i,": ",sum)
