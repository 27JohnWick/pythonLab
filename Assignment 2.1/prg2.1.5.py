st=int(input("Enter the startig range :"))
en=int(input("Enter the ending range :"))
for i in range(st,en):
    if i==1:
        continue
    prime=True
    cnt=0
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            prime=False
    if(prime):
        print(i," is a prime number ")
            
        
