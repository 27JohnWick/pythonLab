units=int(input("Enter the units of electricity bill: "))
s=1
amt=0
if units<=100:
    print("No Charge")
elif 200<=(units-200):
    amt=(units-100)*5
else:
    amt=(100*5)+(units-200)*10
print("The total amount is ", amt)
    
