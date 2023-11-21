string = input("Enter a string: ")
shift=3

eString = ""
dString = ""

for char in string:
    if char.isalpha():
        shift_amount = shift % 26
        if char.islower():
            eChar = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            dChar = chr(((ord(eChar) - ord('a') - shift_amount) % 26) + ord('a'))
        else:
            eChar = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            dChar = chr(((ord(eChar) - ord('A') - shift_amount) % 26) + ord('A'))
    else:
        eChar = char
        dChar = char

    eString += eChar
    dString += dChar

print("String after encryption:", eString)
print("String after decryption:", dString)
