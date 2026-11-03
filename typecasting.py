# typecasting and
# conversion of one datatype to; another is called as type casting
# there are two types of type casting in python
# 1. Implicit type casting:where python itself converts one datatype to another datatype without any user involvement
# 2. Explicit type casting:where user converts one datatype to another datatype using built-in functions like int(), float(), str(), etc.

name ="jhon"
age= 25
print(type(name))

# converting integer to float
a="123"
b=1.23
print(type(a))
print(type(b))
a = int(a)
print("after conversion",type(a))
c= a+b
print(c)
print(type(c))