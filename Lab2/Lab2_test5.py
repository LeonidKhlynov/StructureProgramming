print("Task 5")
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
bl = False
if (a==b)or(a==c)or(b==c):
    bl = True
if bl:
    print('Success')
else:
    print('Error')
