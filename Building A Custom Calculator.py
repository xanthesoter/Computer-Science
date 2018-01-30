#Building a custom calculator

print("This program calculates mpg.")
while True:
    milesDriven = float(input("Enter miles driven: "))
    gallonsUsed = float(input("Enter gallons used: "))
    mpg = milesDriven / gallonsUsed
    print("Miles per gallon: ", mpg)
    answer = input("Do you need another calculation?")
    if answer == "Yes" or answer == "yes" or answer == " yes" or answer == " Yes":
       continue
    else:
       break
