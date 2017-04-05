ar = input("Enter string: ")
ar = ar + " "
wrd = 0
for i in range(1,len(ar)):
    if (ar[i] == " ")and(ar[i-1] != " "):
        wrd = wrd + 1
print("Words: ", wrd)



