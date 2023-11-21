lst = [int(item) for item in input("Enter the list items with space separated : ").split()]
vl=int(input("Enter a value: "))
for ele in lst:
    if ele>vl:
        print(ele," is greater than ",vl)
        
