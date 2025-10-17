# Bytearray: Full Demonstration

# 1. Creating bytearrays
b1 = bytearray()                          # Empty bytearray
b2 = bytearray(5)                         # Bytearray of size 5, initialized with zeros
b3 = bytearray(b'hello')                 # From bytes
b4 = bytearray([65, 66, 67])             # From list of integers
b5 = bytearray("world", "utf-8")         # From string with encoding

# 2. Accessing and modifying elements
print("Original:", b3)                   # bytearray(b'hello')
b3[0] = ord('H')                         # Modify first byte
print("Modified:", b3)                   # bytearray(b'Hello')

# 3. Appending and extending
b3.append(ord('!'))                      # Add one byte
b3.extend(b'!!')                         # Add multiple bytes
print("Appended:", b3)                   # bytearray(b'Hello!!!')

# 4. Slicing and deleting
slice_b3 = b3[1:5]                        # Slice
print("Slice:", slice_b3)                # bytearray(b'ello')
del b3[-1]                               # Delete last byte
print("After delete:", b3)               # bytearray(b'Hello!!')

# 5. Conversion
as_bytes = bytes(b3)                     # Convert to immutable bytes
as_str = b3.decode('utf-8')              # Convert to string
print("As bytes:", as_bytes)
print("As string:", as_str)

# 6. Useful methods
b6 = bytearray(b"abcabc")
print("Count 'a':", b6.count(ord('a')))  # Count occurrences
print("Find 'b':", b6.find(ord('b')))    # Find index
b6.reverse()                             # Reverse in-place
print("Reversed:", b6)

# 7. Clearing and copying
b6_copy = b6.copy()
b6.clear()
print("Cleared:", b6)
print("Copy:", b6_copy)

# 8. Memory view (advanced)
mv = memoryview(b6_copy)
print("Memory view:", mv[0])             # Access via memoryview