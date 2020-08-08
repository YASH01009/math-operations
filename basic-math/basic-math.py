def add(a,b,c=0):
    return a+b+c

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

print(add(a,b))
print(subtract(a,b))
print(multiply(a,b))
print(divide(a,b))
