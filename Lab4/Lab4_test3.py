print('Task 3')
print()
s = input('Enter s: ')
s1 = ""
for i in range(len(s)):
    if s[i]=='*':
        s1 += str(i+1)
    else:
        s1 += s[i]
print("s: ",s1)