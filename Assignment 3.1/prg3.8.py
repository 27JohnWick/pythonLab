string=input("Enter a sring: ")
n=(len(string)+1)
ft=0
while(n):
    if ft==0:
        print(string[ft: :])
        ft+=1
        n-=1
    else:
        print(string[ft: :]+string[0:ft])
        ft+=1
        n-=1
    
