string=input("Enter a string :")
print("String Before is: ",string)
fchar,lchar=string[0],string[-1]
string1=lchar+string[1:-1]+fchar
print("String After is: ",string1)
