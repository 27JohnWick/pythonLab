credits=int(input("Enter how many number of credits you have: "))
if(credits <= 23):
    print("The student is a freshman")
elif(credits > 23 and credits <= 53):
    print("You are a Sophomore")
elif(credits >= 54 and credits <= 83):
    print("You are junior")
else:
    print("Wow!!You are senior")
    
