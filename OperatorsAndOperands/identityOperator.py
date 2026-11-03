# identity operators are used to compare the memory locations of two objects. They are 'is' and 'is not'.
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # False, because x and y are two different objects in memory
z = x
print(x is z)  # True, because z is a reference to the same object as x 
print(x is not y)  # True, because x and y are two different objects in memory
print(x is not z)  # False, because z is a reference to the same object as x
print(x == y)  # True, because x and y have the same content, even though they are different objects
print(x != y)  # False, because x and y have the same content, even though they are different objects