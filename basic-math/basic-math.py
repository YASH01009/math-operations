def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print("The sum is " + add(a,b))
print("The difference is " + subtract(a,b))
print("The product is " + multiply(a,b))
print("The quotient is " + divide(a,b))
