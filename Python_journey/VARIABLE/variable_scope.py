# Variable Scope Example

x = 10  # global variable

def show_number():
    x = 5  # local variable
    print("Inside function:", x)

show_number()
print("Outside function:", x)
x = 20  # updating global variable
print("Updated global variable:", x)