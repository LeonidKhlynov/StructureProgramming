print('Task 2')
print()
s = input('Enter s: ')
s1 = ""
s2 = ""
for i in range(len(s)):
    if (i+1)%2==0:
        s2 = s2 + s[i]
    else:
        s1 = s1 + s[i]
print("Nechetnie: ",s1)
print("Chetnye: ",s2)