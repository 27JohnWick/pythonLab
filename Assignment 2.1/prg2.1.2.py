numb=int(input("Enter the number :"))
cnt=0
cnt=numb%10
if(cnt%3)==0:
    print("The last digit is divisible by 3")
else:
    print("The last digit is not divisible by 3")
