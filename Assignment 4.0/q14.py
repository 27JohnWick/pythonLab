string = input("Enter the string: ")
nstr = ""
for wrd in string.split():
    nstr += wrd[0].upper() + wrd[1:-1] + wrd[-1].upper() + " "
print("New string after capitalizing first and last letters of each word: ", nstr.strip())
