"""def add(a, b):
    # Keep adding 'b' to 'a' until 'b' becomes 0
    while b != 0:
        carry = a & b  # Calculate the carry using bitwise AND
        a = a ^ b      # Calculate the sum without considering the carry using bitwise XOR
        b = carry << 1  # Shift the carry one position to the left
    return a

# Test the function
result = add(5, 7)
print(result)  # Output: 12"""

#!/usr/bin/env python3
#add = __import__('0-sum').add

def add(a,b):
    return a+b
print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

add(5,7)