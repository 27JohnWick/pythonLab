str1=input("Enter a string: ")
snot = str1.find('not')
spoor = str1.find('poor')
if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    print(str1)
else:
    print(str1)

