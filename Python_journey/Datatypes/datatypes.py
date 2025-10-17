# Integer
integer_var = 10

# Float
float_var = 10.5

# String
string_var = "Hello, World!"

# Boolean
bool_var = True

# List
list_var = [1, 2, 3, 4, 5]

# Tuple
tuple_var = (1, 2, 3, 4, 5)

# Set
set_var = {1, 2, 3, 4, 5}

# Dictionary
dict_var = {"name": "Alice", "age": 25}

# NoneType
none_var = None

# Bytes
bytes_var = b'Hello'

# Bytearray
bytearray_var = bytearray([65, 66, 67])

# Complex
complex_var = 2 + 3j

# Print all variables and their types
variables = [
    integer_var, float_var, string_var, bool_var, list_var,
    tuple_var, set_var, dict_var, none_var, bytes_var,
    bytearray_var, complex_var
]

for var in variables:
    print(f"{var} -> {type(var)}")