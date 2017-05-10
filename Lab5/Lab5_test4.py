def inp(a,n,m):
    for i in range(0,n):
        a.append([])
        for j in range(0,m):
            a[i].append(int(input("Enter matrix number: ")))

def outp(a,n,m):
    sum = 0
    print('Matrix')
    for i in range(0,n):
        for j in range(0,m):
            print(a[i][j],end=' ')
            if i==1:
                sum += a[i][j]
        print()
    return print('Second string sum: ',sum)

print('Task 4')
print()
n = int(input('Enter number of parameters: '))
m = n
a = []
sum = 0
inp(a,n,m)
outp(a,n,m)


