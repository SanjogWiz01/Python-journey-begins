# basic_float_operations.py

def add_floats(a: float, b: float) -> float:
    return a + b

def subtract_floats(a: float, b: float) -> float:
    return a - b

def multiply_floats(a: float, b: float) -> float:
    return a * b

def divide_floats(a: float, b: float) -> float:
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")
print(add_floats(1.5, 2.5),
subtract_floats(5.0, 3.0),
multiply_floats(4.0, 2.0),
divide_floats(10.0, 2.0))
# This will raise an exception
# Example usage    