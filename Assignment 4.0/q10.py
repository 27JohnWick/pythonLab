lst = [int(item) for item in input("Enter the list items with space separated : ").split()]
even=[]
odd=[]
for ele in lst:
    if ele%2==0:
        even.append(ele)
    else:
        odd.append(ele)
print("Even list is :",even,"\nOdd list is :",odd)
