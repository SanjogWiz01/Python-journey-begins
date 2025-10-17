# Create a bytearray
data = bytearray(b'hello')

# Create a memoryview of the bytearray
mv = memoryview(data)

# Access elements
print(mv[0])          # 104 (ASCII for 'h')

# Slice without copying
print(mv[1:4].tobytes())  # b'ell'

# Modify original data via memoryview
mv[0] = ord('H')
print(data)           # bytearray(b'Hello')