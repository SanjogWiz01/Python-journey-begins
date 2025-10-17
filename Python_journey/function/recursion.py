def fact(x):
 if x < 0:
        return "Factorial does not exist for negative numbers."
    
 elif x == 0 or x == 1:
        return 1
 else:
        return x * fact(x - 1)

x = int(input("Enter the number you want factorial of: "))
print("The factorial is:", fact(x))
# Example usage:
# print(fact(5))  # Output: 120