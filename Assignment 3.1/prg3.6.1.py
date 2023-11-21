string = input("Enter a string: ")
st = ""
st1 = ""

print("String before encoded is:", string)

for i in string:
    if ord(i) == 65:
        st += chr(65 - 3)
    elif ord(i) == 66:
        st += chr(66 - 3)
    elif ord(i) == 67:
        st += chr(67 - 3)
    elif ord(i) == 92:
        st += chr(92 - 3)
    elif ord(i) == 93:
        st += chr(93 - 3)
    elif ord(i) == 94:
        st += chr(94 - 3)
    elif i == " ":
        st += " "
    else:
        st += chr(ord(i) - 3)

print("String after encoded is:", st)

st1 = ""

for i in string:
    if ord(i) == 62:
        st1 += chr(59 + 3)
    elif ord(i) == 61:
        st1 += chr(58 + 3)
    elif ord(i) == 60:
        st1 += chr(57 + 3)
    elif ord(i) == 33:
        st1 += chr(30 + 3)
    elif ord(i) == 32:
        st1 += chr(29 + 3)
    elif ord(i) == 31:
        st1 += chr(28 + 3)
    elif i == " ":
        st1 += " "
    else:
        st1 += chr(ord(i) + 3)

print("String after Decipher is:", st1)
