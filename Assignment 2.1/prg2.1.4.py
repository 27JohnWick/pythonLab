sal=float(input("Enter the salary of the employee:"))
exp=int(input("Enter the years of service :"))
if exp>10:
    print("The salary is :",(sal*(10/100))+sal)
elif(exp>=6 and exp<=10):
    print("The salary is :",(sal*(8/100))+sal)
elif exp>6:
    print("The salary is :",(sal*(5/100))+sal)
