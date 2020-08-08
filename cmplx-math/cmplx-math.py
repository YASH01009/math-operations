def add(l):
    res = 0
    for a in l:
        res += a
    return res

def subtract(s,l):
    for a in l:
        s -= a
    return s

def multiply(l):
    res = 1
    for a in l:
        res *= a
    return res

def divide(s,l):
    for a in l:
        s /= a
    return s

s = 120
l = [1,2,3,4,5]

print(add(l))
print(subtract(s,l))
print(multiply(l))
print(divide(s,l))
