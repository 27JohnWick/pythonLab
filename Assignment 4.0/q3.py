lst = [int(item) for item in input("Enter the list items with space separated : ").split()]
mx,mi=max(lst),min(lst)
print("Maximum element in the list is: ",lst.index(mx),"\nMinimum of the list is: ",lst.index(mi))
