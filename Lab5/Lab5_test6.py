def inp(a,n,m):
    for i in range(0,n):
        a.append([])
        for j in range(0,m):
            if (i==4)or(i==0):
               if (j%2==0):
                   a[i].append(1)
               else:
                   a[i].append(0)
            else:
                if (i==1)or(i==3):
                    if (j==0)or(j==4):
                        a[i].append(0)
                    else:
                        a[i].append(1)
                else:
                    if (i==2):
                        if (i==j):
                            a[i].append(0)
                        else:
                            a[i].append(1)

print('Task 6')
print()
a = []
n = m = 5
inp(a,n,m)
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()
