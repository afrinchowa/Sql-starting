# datatypes and user inputs 
# datatypes= text, number, boolean, list, tuple, set, dictionary

# user inputs= input() function is used to take user inputs in Python. The input() function takes a string as an argument and displays it as a prompt to the user. The user can then enter a value, which is returned as a string.

name= input("Enter your name: ")
print("Hello " + name + "! Welcome to the program.")
age= input("Enter your age: ")
print("You are " + age + " years old.")
age= int(input("Enter your age: "))
print("You are " + str(age) + " years old.")
height= float(input("Enter your height in meters: "))
print("You are " + str(height) + " meters tall.")
exp1 =eval(input("Enter your experience in years: "))
print("You have " + str(exp1) + " years of experience.")