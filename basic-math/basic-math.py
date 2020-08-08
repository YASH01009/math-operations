'''This function adds numbers'''
def add(a,b):
    return a+b

'''This function subtracts numbers'''
def subtract(a,b):
    return a-b

'''This function multiplies numbers'''
def multiply(a,b):
    return a*b

'''This function divides numbers'''
def divide(a,b):
    return a/b

'''Taking input from the user'''
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
x = int(input("Enter the third number : "))

'''Displaying output for the user'''
print("The results are ")
print("sum : " + add(a,b))
print("difference : " + subtract(a,b))
print("product : " + multiply(a,b))
print("quotient : " + divide(a,b))
