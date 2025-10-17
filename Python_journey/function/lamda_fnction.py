# Lambda (anonymous) function

square = lambda x: x**2
print("Square of 5:", square(5))
add = lambda a, b: a + b
print("Sum of 3 and 4:", add(3, 4))

multiply = lambda a, b: a * b
print("Product of 6 and 7:", multiply(6, 7))
greet = lambda name: f"Hello, {name}!"
print(greet("Alice"))
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)