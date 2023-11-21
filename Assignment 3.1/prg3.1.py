string= input("Enter a string: ")
cnt=0
vowel="aeiouAEIOU"
for i in string:
    if i in vowel:
        cnt+=1
print("The no of vowel in the string ", string,"is ",cnt)
