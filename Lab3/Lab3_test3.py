print('Task 3')
print()
k = int(input('Enter k: '))
pr = 1
sm = 0
for j in range(-3,k):
	pr = pr * ((j+2)*j)/j-3
	for i in range(j,k+5):
		sm = sm + (i+5)/((i-11)-3.5*i)
print('p: ',pr)
print('s: ',sm)
print('Result: ',pr*sm)

