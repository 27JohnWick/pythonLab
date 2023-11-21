mDays = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
mName = input("Enter a month name: ")
print(mDays[mName])
print(sorted(mDays.keys()))
print([month for month, days in mDays.items() if days == 31])
print([(days, month) for month, days in mDays.items()])
