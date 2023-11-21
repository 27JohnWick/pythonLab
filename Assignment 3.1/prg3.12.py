string=input("Enter a string :")
end=len(string)
n=string.find(string[0],1,end)
s=""
for i in range(end):
    if n==i:
        s+="$"
    else:
        s+=string[i]
print(s)
