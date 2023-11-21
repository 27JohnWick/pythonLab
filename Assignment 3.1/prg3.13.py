string=input("Enter a string :")
s=""
s1=""
for i in string:
    if i==" ":
        s1=s
        s=""
    else:
        s+=i
sSize=len(s)
s1Size=len(s1)
stin=s[0:sSize-1]+s1[-1]+" "+s1[0:s1Size-1]+s[-1]
print(stin)
