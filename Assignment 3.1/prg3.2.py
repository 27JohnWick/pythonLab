string= input("Enter a string: ")
upr=0
lwr=0
d=0
wh=0
for i in string:
    if i.isupper():
        upr+=1
    elif i.islower():
        lwr+=1
    elif i.isdigit():
        d+=1
    elif i==" ":
        wh+=1
print("The no of upper letter are",upr," lower are",lwr,"digit are",d,"White space are",wh)
