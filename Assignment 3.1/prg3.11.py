string=input("Enter a string: ")
if len(string)<2:
   print("String is Empty")
elif len(string)==2:
    print(string*2)
else:
    s=string[0:2]+string[-2:]
    print(s)
    
