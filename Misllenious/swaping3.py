no1=int(input("Enter the no 1: "))
no2=int(input("Enter the no 2: "))
no3=int(input("Enter the no 3: "))
print("The value of no1 is",no1,"no2 is",no2,"and no3 is ",no3) 
no1=no1+no2+no3
no2=no1-(no2+no3)
no3=no1-(no2+no3)
no1=no1-(no2+no3)
print("After swapping he value of no1 is",no1,"no2 is",no2) 
