def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
    
print(add(5, 3))
print(subtract(10, 4))
print(multiply(6, 7))
print(divide(8, 2))