f = 2.75
ratio = f.as_integer_ratio()
print(ratio)
f = 5.5
print(f.conjugate())
s = "0x1.91eb851eb851fp+1"
a = float.fromhex(s)
print(a)
f = 3.14
print(f.hex())
print((4.0).is_integer())  
print((4.5).is_integer())
f = -7.3
print(f.__abs__())  
print(abs(f))
a = 5.5
b = 2.2
print(a.__add__(b))  
print(a + b)
print(a.__sub__(b))  
print(a - b)
print(a.__mul__(b))
print(a * b)
a = 7.5
b = 2.5
print(a.__floordiv__(b))   
print(a // b)
print(a.__truediv__(b))  
print(a / b)# print(divide_floats(10.0, 0.0))  # Uncommenting this line will raise an exception