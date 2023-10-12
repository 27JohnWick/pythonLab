a=float(input("Enter first side of a triangle: "))
b=float(input("Enter second side of a triangle: "))
c=float(input("Enter third side of a triangle: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle: ",area)
