# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num == 3:
#         pass  # Skip processing when num is 3
#     else:
#         print(f"Processing number: {num}")

def print_numbers(n):
 for i in range(1, n+1):
        if i == 2:
            pass
        else:
            print(i)
n = int(input("enter the number"))
print_numbers(n)
#         print("*"*i)
#         print(" "*(n-i)+"*"*i)