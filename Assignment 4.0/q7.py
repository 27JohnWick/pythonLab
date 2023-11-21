lst = [int(item) for item in input("Enter the list items with space separated : ").split()]
lst.sort()
res = []
for i in lst:
    if i not in res:
        res.append(i)
print("Second Smallest is ",res[1],"\nSecond Largest is ",res[-2])
