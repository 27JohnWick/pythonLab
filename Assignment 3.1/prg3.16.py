string=input("Enter a string :")
s=""
s1=""
size=0
for i in string:
    if i==" ":
        s1=s
        if size<len(s1):
            size=len(s1)
        s=""
    else:
        s+=i
        
if size<len(s):
    size=len(s)
    print("Length of the longest word: ",size)
else:
    print("Length of the longest word: ",size)

