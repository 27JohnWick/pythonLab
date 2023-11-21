string=input("Enter your password: ")
up,lw,dg=0,0,0
if(len(string) >= 8):
    for i in string:
        if(i.islower()):
            lw+=1
        if(i.isupper()):
            up+=1
        if(i.isdigit()):
            dg+=1
    if (lw>=1 and up>=1 and dg>=1 and lw+up+dg==len(string)):
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Enter a valid password.")
