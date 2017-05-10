print('Task 5')
print()
a = []
sum = 0
n = int(input('Enter number of parameters: '))
m = n
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(int(input('Enter matrix number: ')))
        if j > i:
            sum += a[i][j]
print('Matrix')
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()
print('Sum above the main diagonal: ',sum)