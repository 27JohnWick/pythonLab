my_list = [('B', 68), ('D', 70), ('A', 67), ('C', 69)]
order = ['A', 'B', 'C', 'D']
result = sorted(my_list, key=lambda x: order.index(x[0]))
print(result)
