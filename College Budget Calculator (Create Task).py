# College Budget Calculator

import time

print(time.asctime())

print("Create an account and login before you can run the calculator.")

def username():
    username = input("Enter what you would like your username to be: ")
    print("Username created successfully")
    print(" ")
    return username
def password():
    password = input("Enter what you would like your password to be: ")
    print("Password created successfully")
    print(" ")
    return password

username = username()
password = password()

def login():
    total_triesUser=0
    total_triesPass=0
    print("Your account was created successfully now you must login.")
    print(" ")
    while total_triesUser<4 and total_triesPass<4:      
        theUsername = str(input("Enter your username, the press Return/Enter: "))
        if theUsername == username:
            total_triesUser+=4
            print("Username successful")
            print(" ")
            while total_triesPass<4:
                thePassword=str(input("Enter the password, then press Return/Enter: "))
                if thePassword == password:
                    total_triesPass+=4
                    print("Password successful")
                    print(" ")
                else:
                    print("Unable to log in. ")
                    total_triesPass+=1
                    if total_triesPass>3:
                        print("You have been locked out from attempting to login too many times.")
                        print(" ")
                        break
        else:
            print("Username Incorrect.")
            total_triesUser+=1
            if total_triesUser>3:
                print("You have been locked out from attempting to loging too many times.")
                print(" ")
                break

login()

while True:
    print('''Welcome to the college calculator!
Follow the questions and in the end a reciept based on your anwsers will be printed.''')
    def tuition():
        userInput = int(input("How much is tuition?: "))
        return userInput
    def room():
        userInput = input("""Dorm room types:
                                    A. Single
                                    B. Double
                                    C. Triple
                                    D. Single Suite
                                    E. Multiple-occupancy Suite
                                    F. Apartment
                                    Which type of room do you want to dorm in?: """)
        if userInput == "A" or userInput == "a":
            return 12194
        elif userInput == "B" or userInput == "b":
            return 11356
        elif userInput == "C" or userInput == "c":
            return 10793
        elif userInput == "D" or userInput == "d":
            return 13304
        elif userInput == "E" or userInput == "e":
            return 11627
        elif userInput == "F" or userInput == "f":
            return 13239
        else:
            print("That isn't an option.")
            return room()

    def meal_plan():
        userInput = input("""Meal Plans:
                                    A. Regular 5
                                    B. Regular 10
                                    C. Premium 5
                                    D. Premium 10
                                    E. Unlimited
                                    What type of meal plan do you want?: """)
        if userInput == "A" or userInput == "a":
            return 245
        elif userInput == "B" or userInput == "b":
            return 345
        elif userInput == "C" or userInput == "c":
            return 350
        elif userInput == "D" or userInput == "d":
            return 450
        elif userInput == "E" or userInput == "e":
            return 550
        else:
            print("That isn't an option.")
            return meal_plan()
        
    def books():
        userInput = input("Do you plan on purchasing hardcopies or digital copies of your books? Enter A for hardcopy or B for digital: ")
        if userInput == "A" or userInput == "a":
            userInput = input("Are you purchasing from our library or from an outside source? Enter A for from the school or B for outside: ")
            if userInput == "A" or userInput == "a":
                userInput = input("Do you want a new or used copy? Enter A for new or B for used: ")
                if userInput == "A" or userInput == "a":
                    return 2000
                elif userInput == "B" or userInput == "b":
                    return 1000
            elif userInput == "B" or userInput == "b":
                userInput = input("Do you want a new or used copy? Enter A for new or B for used: ")
                if userInput == "A" or userInput == "a":
                    return 3150
                elif userInput == "B" or userInput == "b":
                    return 1900
        elif userInput == "B" or userInput == "b":
            return 950
        else:
            print("That isn't a value.")
            return books()

    def spending_money():
        userInput = int(input("How much do you plan to bring to spend per month?: "))
        cost = userInput * 9
        return cost
 
    def travel():
        userInput = int(input("How far away from campus do you live? Enter distance in miles: "))
        if userInput <= 50:
            return 100
        elif userInput <= 100:
            return 250
        elif userInput <= 500:
            return 700
        elif userInput <= 1000:
            return 2000
        elif userInput > 1000:
            return 3000
        else:
            print("That isn't an option.")
            return travel()

    def deductions():
        scholarship = int(input("Did you get any scholarships, grants, awards, etc.? Enter the total here: "))
        loans = int(input("How much are you taking out in loans?: "))
        totaldeductions = scholarship + loans
        return totaldeductions

    def fees():
        return 800

    def reciept(tuition_and_fees, room_and_board, books, spending_money, travel, total_deductions, cost):
        print("")
        print("RECIEPT:")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("| Tuition and Fees: $",tuition_and_fees)
        print("| Room and Board: $",room_and_board)
        print("| Books: $",books)
        print("| Spending Money: $",spending_money)
        print("| Travel Expenses: $",travel)
        print("| Total Aid: $",total_deductions)
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your expected fall 2018/2019 cost: $",cost)

    tuition_and_fees = tuition() + fees()
    room_and_board = room() + meal_plan()
    books = books()
    spending_money = spending_money()
    travel = travel()
    total_deductions = deductions()
    cost = tuition_and_fees + room_and_board + books + spending_money + travel - total_deductions

    reciept(tuition_and_fees, room_and_board, books, spending_money, travel, total_deductions, cost)



    answer = input("Do you want to calculate the cost again?: ")
    if answer == "Yes" or answer == "yes" or  answer == "Y" or answer == "y":
        continue
    else:
        print("Have fun being in debt!")
        break
