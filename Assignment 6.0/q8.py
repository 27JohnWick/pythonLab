employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = {employee: defaults for employee in employees}
print(result)
