#Function Returning Multiple Values

def arithmetic_operations(a, b):
    return a + b, a - b, a * b, a / b


add, subtract, multiply, divide = arithmetic_operations(10, 5)
print(f"Add: {add}, Subtract: {subtract}, Multiply: {multiply}, Divide: {divide}")
