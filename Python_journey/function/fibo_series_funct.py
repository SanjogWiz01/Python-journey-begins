def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

# Example: print first 10
print([fib_rec(i) for i in range(10)])
