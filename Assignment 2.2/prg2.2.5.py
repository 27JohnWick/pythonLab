items=int(input("Enter how many items you buy: "))
if items < 10:
    total_cost= 12 * items
    print("Total Cost: ",total_cost)
elif items > 10 and items < 99:
    total_cost= 10 * items
    print("Total Cost: ",total_cost)
elif items >= 100:
    total_cost= 7 * items
    print("Total Cost: ",total_cost)
else:
    print("THANK YOU FOR VISITING")
