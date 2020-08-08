def add(a,b,c=0):
    return a+b+c

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

print("The results are ")
print("sum : " + add(a,b))
print("difference : " + subtract(a,b))
print("product : " + multiply(a,b))
print("quotient : " + divide(a,b))
