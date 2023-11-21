string = input("Enter the string: ")
cnt = 0
vw = []
for ele in string:
    if ele in "aeiou":
        cnt += 1
        vw.append(ele)
print("The number of vowels present in the text:", cnt,"vowels are:",vw)
