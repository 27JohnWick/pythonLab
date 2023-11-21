string=input("Enter a string :")
n=len(string)
if n>=3:
    if string[-3:]=="ing":
        s=string+"ly"
        print(s)
    else:
        s=string+"ing"
        print(s)
else:
    print(string)
