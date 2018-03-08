# The Camel Game

print("You have stolen a camel and the only way to survive is make it acrosss the Mobi desert.")
print("The natives are upset that you have the camel so they are hunting you down.")
print("In order to win you must survive the trek across the desert and outrun those natives")
print("")
print("Your thirst level, the camels fatigue level and distance from the natives will be tracked throughout the game")
print("")


miles_travelled = 0
miles_travelled = int(miles_travelled)
thirst = 0
thirst = int(thirst)
camel_tiredness = 0
camel_tiredness = int(camel_tiredness)
natives = -20
natives = int(natives)
canteen = 4
canteen = int(canteen)
done = True


import random
def randNumNatives():
    for x in range(1):
        print(random.randint(6, 15))

def randNum2FSpeed():
    for x in range(1):
        print(random.randint(9, 21))

def randNum3Camel():
    for x in range(1):
        print(random.randint(1, 4))

def randNum4MSpeed():
    for x in range(1):
        print(random.randint(4, 13))
        
while True:
    print("A. Drink from your canteen")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit")
    
    answer = input("Your choice?: ")
    if answer == "Q" or answer == "q":
        print("Thanks for playing!")
        break
    elif answer == "E" or answer == "e":
        print("Miles travelled:",miles_travelled)
        print("Thirst levels:",thirst)
        print("Camel tiredness levels:",camel_tiredness)
        print("Drinks in canteen:",canteen)
        print("The natives are",natives,"miles behind you")
    elif answer == "D" or answer == "d":
        camel_tiredness = 0
        print("The camel is happy")
        natives = natives + randNumNatives()
    elif answer == "C" or answer == "c":
        miles_travelled = miles_travelled + randNum2FSpeed()
        print("You have travelled",miles_travelled,"miles")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + randNum3Camel()
        natives = natives + randNumNatives()
    elif answer == "B" or answer == "b":
        miles_travelled = miles_travelled + randNum4MSpeed()
        print("You have travelled",mies_travelled,"miles")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + randNum3Camel()
        natives = natives + randNumNatives()
    elif answer == "A" or answer == "a":
        canteen = canteen - 1
        print("You have",canteen,"drinks left")
    if not done and thirst > 4:
        print("You are thirsty.")
    elif not done and thirst > 6:
        print("You have died of thirst!")
        break
    if not done and camel_tiredness > 5:
        print("Your camel is getting tired.")
    elif not done and camel_tiredness > 8:
        print("Your camel is dead.")
        break
    if not done and natives >= miles_travelled:
        print("The natives have caught up and you are now dead.")
        break
    elif not done and natives + 15 >= miles_travelled:
        print("The natives are getting close!")
    if not done and miles_traveled >= 200:
        print("You have crossed the desert. You've won!")
        print("You have also stumbled across an oasis.")
        miles_travelled = 0
        thirst = 0
        camel_tiredness = 0
        canteen = 4
    play_again = input("Do you want to play again?: ")
    if play_again == "Yes" or play_again == "yes" or play_again == "Y" or play_again == "y":
        continue
    else:
        print("Thanks for playing!")
        break
