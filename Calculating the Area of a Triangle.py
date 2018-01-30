# Calculating the Area of a Rectangle

print("This program calculates the area of a rectangle.")
while True:
    length = float(input("Enter the length of rectangle:"))
    width = float(input("Enter the width of rectangle: "))
    Area = length * width
    print("The area of the rectangle is:", Area)
    answer = input("Do you need another calculation?")
    if answer == "Yes" or answer == "yes" or answer == " yes" or answer == " Yes":
       continue
    else:
       break
