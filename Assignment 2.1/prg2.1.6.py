numb=int(input("Enter a number:"))
if(numb% 5==0 and numb%3==0):
    print("FizzBuzz")
elif numb%3==0:
    print("Fizz")
elif numb%5==0:
    print("Buzz")
else:
    print(numb)
    
