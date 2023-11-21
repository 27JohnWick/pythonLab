string=input("Enter the string: ")
s=""
le=len(string)
for i in range(le):
    if i%2==0:
        s+=string[i]
print(s)
