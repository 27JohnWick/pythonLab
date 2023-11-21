string=input("Enter a string: ")
le=len(string)
n=int(input("Enter the index of the character from the string:"))
if n>le:
    print("Can't remove the character/Out of Index")
else:
    s1=string.replace(string[n],"")
    print(s1)
