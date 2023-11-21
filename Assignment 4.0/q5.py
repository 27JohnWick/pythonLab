lst1 = [int(item) for item in input("Enter the list items with space separated : ").split()]
lst2 = [int(item) for item in input("Enter the list items with space separated : ").split()]
for ele in lst1:
    if ele in lst2:
        print(ele," is common")
        
