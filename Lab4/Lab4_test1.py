print('Task 1')
print()
s = input()
i = 0
while i < len(s):
    if (s[i] == '.'):
        s = s[:i+1] + '.' + s[i+1:]
        i += 2
    else:
        i += 1
print(s)