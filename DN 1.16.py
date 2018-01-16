n = 1
m = -1
if n < -m:
    print(n)
else:
    print(m)

from math import sqrt
x = sqrt(2.0)
y = 2.0
if x*x==y:
    print(x)
else:
    print(y)
  
# Using input() to make an interactive progtam
numbers = float(input("Enter the number you want to square root: "))
numb_squared = sqrt(numbers)
print("Your number is:", numb_squared)
