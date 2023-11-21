list1 = ['Hi', 'Good Morning']
list2 = ['John', 'Allen', 'Kelly']

result = [greeting + name for greeting in list1 for name in list2]
print(result)
