# write a program to check if a number is positive

num= int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    
    # write a program to check whether a number is even or odd
    num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
    # write a program to create a area calculator using if else statement
print("Area Calculator")
print("""press 1 for area of circle
   press 2 for area of rectangle
   press 3 for area of triangle
   press 4 for area of square""")

choice = int(input("Enter your choice: "))
if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius * radius
    print("The area of the circle is:", area)
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print("The area of the rectangle is:", area)
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)
elif choice == 4:
    side = float(input("Enter the side of the square: "))
    area = side * side
    print("The area of the square is:", area)
else :
    print("Invalid choice. Please select a valid option.")
    # write a program to check whether the passed letter is a vowel or consonant
letter = input("Enter a letter: ").lower()
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("The letter is a vowel.")
else:
    print("The letter is a consonant.")
    
    # write a program to check if a number is a single digit or double digit or triple digit , 2 digit number and so on... up to 5 digits
num = int(input("Enter a number: "))
if num < 10:
    print("The number is a single digit.")
elif num < 100:
    print("The number is a double digit.")
else:
    print("The number is a triple digit.")
    
    
    
  