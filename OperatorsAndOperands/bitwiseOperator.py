# Bitwise operators are used to perform bit-level operations on binary numbers. The bitwise operators in Python are:
# AND (&): Performs a bitwise AND operation on two integers. Each bit of the output
# is 1 if the corresponding bits of both operands are 1, otherwise it is 0.
# OR (|): Performs a bitwise OR operation on two integers. Each bit of the output is 1 if at least one of the corresponding bits of the operands is 1, otherwise it is 0.
# XOR (^): Performs a bitwise XOR operation on two integers. Each bit of the output is 1 if the corresponding bits of the operands are different, otherwise it is 0.
# NOT (~): Performs a bitwise NOT operation on an integer. It flips the bits of the integer, changing 1s to 0s and 0s to 1s.
# Left Shift (<<): Shifts the bits of the first operand to the left by the number of positions specified by the second operand. This is equivalent to multiplying the first operand by 2 raised to the power of the second operand.
# Right Shift (>>): Shifts the bits of the first operand to the right by the number of positions specified by the second operand. This is equivalent to dividing the first operand by 2 raised to the power of the second operand.
# Example usage of bitwise operators:



x = 10  # Binary: 1010
print(x & 3)  # Bitwise AND: 1010 & 0011 = 0010 (2 in decimal)
print(x | 3)  # Bitwise OR: 1010 | 0011 = 1011 (11 in decimal)
print(x ^ 3)  # Bitwise XOR: 1010 ^ 0011 = 1001 (9 in decimal)
print(~x)     # Bitwise NOT: ~1010 = 0101 (in two's complement, this is -11 in decimal)
# print(x << 2) # Left Shift: 1010 << 2 = 101
# 0 (40 in decimal)
print(x >> 2) # Right Shift: 1010 >> 2 = 0010 (2 in decimal)
print(bin(x))  # Binary representation of 10

a=9
b=10
print(a&b) # Bitwise AND: 1001 & 1010 = 1000 (8 in decimal)
print(a|b) # Bitwise OR: 1001 | 1010 =  1011 (11 in decimal)
print(a^b) # Bitwise XOR: 1001 ^ 1010 = 0011 (3 in decimal)
print(bin(a))  # Binary representation of 9
print(bin(b))  # Binary representation of 10
# zero fill left shift
print(b<<2) # Left Shift: 1010 << 2 = 101000
# zero fill right shift
print(b>>2) # Right Shift: 1010 >> 2 = 0010 (2 in decimal)
