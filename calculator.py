# This is a simple calculator program
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero error"
    
#user input for operation
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(x, "+", y, "=", add(x, y))
elif operation == "-":
    print(x, "-", y, "=", subtract(x, y))
elif operation == "*":
    print(x, "*", y, "=", multiply(x, y))
elif operation == "/":
    print(x, "/", y, "=", divide(x, y))
else:
    print("Invalid operation")