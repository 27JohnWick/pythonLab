p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time: "))
SI=(p*r*t)/100
CI=p*(1+r/100)**t - p
print("Simple Interest: ",SI,"\nCompound Interest: ",CI)
