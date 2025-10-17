# Simple Calculator using Functions

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Cannot divide by zero"

def calculator():
    print("=== Functional Calculator ===")
    print("Choose operation: +  -  *  /")
    op = input("Enter operator: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operations = {"+": add, "-": sub, "*": mul, "/": div}
    result = operations.get(op, lambda a, b: "Invalid operator")(a, b)
    print("Result:", result)

calculator()
