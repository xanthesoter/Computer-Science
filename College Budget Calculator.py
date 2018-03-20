# College Budget Calculator for
# books, spending money, travel, loans, scholarships, grants, fees

import random
import time

print(time.asctime())

def authenticate():
     total_triesUser=0
     total_triesPass=0
     while total_triesUser<4 and total_triesPass<4:
          theUsername=str(input("Enter your username, the press Return/Enter: "))
          if theUsername== "Codemaster":
               total_triesUser+=4
               print("Username successful")
               while total_triesPass<4:
                     thePassword=str(input("Enter the password, then press Return/Enter: "))
                     if thePassword== "201010":
                          total_triesPass+=4
                          print("Password successful")
                     else:
                          print("Unable to log in. ")
                          total_triesPass+=1
                          if total_triesPass>3:
                               break                         
          else:
               print("Username Incorrect.")
               total_triesUser+=1
               if total_triesUser>3:
                    break

 True:
    def tuition():
        userInput = input("How much is tuition?: ")
        return(userInput)
    def room():
        userInput = input(""" Dorm room types:
                                    A. Single
                                    B. Double
                                    C. Triple
                                    D. Single Suite
                                    E. Multiple-occupancy Suite
                                    F. Apartment
                                    Which type of room do you want to dorm in?: """)
        if userInput == "A" or userInput == "a":
            return(12,194)
        elif userInput == "B" or userInput == "b":
            return(11,356)
        elif userInput == "C" or userInput == "c":
            return(10,793)
        elif userInput == "D" or userInput == "d":
            return(13,304)
        elif userInput == "E" or userInput == "e":
            return(11,627)
        elif userInput == "F" or userInput == "f":
            return(13,239)                                                
    def meal_plan():
        userInput = input("""Meal Plans:
                                        A. Regular 5
                                        B. Regular 10
                                        C. Premium 5
                                        D. Premium 10
                                        E. Unlimited
                                        What type of meal plan do you want?: """)
        if userInput == "A" or userInput == "a":
            return(245)
        elif userInput == "B" or userInput == "b":
            return(345)
        elif userInput == "C" or userInput == "c":
            return(350)
        elif userInput == "D" or userInput == "d":
            return(450)
        elif userInput == "E" or userInput == "e":
            return(550)
    def books():
        userInput = input("Do you plan on purchasing hardcopies or digital copies of your books? Enter A for hardcopy or B for digital: ")
        if userInput == "A" or userInput == "a":
            userInput = input("Are you purchasing from our library or from an outside source? Enter A for from the school or B for outside: ")
            if userInput == "A" or userInput == "a":
                userInput = input("Do you want a new or used copy? Enter A for new or B for used: ")
                if userInput == "A" or userInput == "a":
                    return(2000)
                elif userInput == "B" or userInput == "b":
                    return(1000)
            elif userInput == "B" or userInput == "b":
                 userInput = input("Do you want a new or used copy? Enter A for new or B for used: ")
                if userInput == "A" or userInput == "a":
                    return(3150)
                elif userInput == "B" or userInput == "b":
                    return(1900)
        elif userInput == "B" or userInput == "b":
            return(950)
    def spending_money():
        userInput = input("How much do you plan to bring to spend per month?: ")
        cost = userInput * 9
        return(cost)
    def travel():
        userInput = input("How far away from campus do you live? Enter distance in miles: ")
        if userInput <= 50:
            return(100)
        elif userInput <= 100:
            return(250)
        elif userInput <= 500:
            return(700)
        elif userInput <= 1000:
            return(2000)
        elif userInput > 1000:
            return(3000)
    def deductions():
        scholarship = float(input("Did you get any scholarships, grants, awards, etc.? Enter the total here: "))
        loans = float(input("How much are you taking out in loans?: "))
        totaldeductions = scholarship + loans
        return(totaldeductions)
    def fees():
        return(800)

"""
    
    discount = input("Do you have a discount code? If so, enter here: ")
    if discount == "15OFF":
        new_total = total - (total * 0.15)
    else:
        new_total = total + 0
    
    tax = 0.07
    total_tax = int(new_total * tax)
    final_total = new_total + total_tax

    print("")
    print("RECIEPT:")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("| Total: $",total)
    print("| Total with any discounts: $",new_total)
    print("| Tax: $",total_tax,)
    print("| Your total trip cost is",final_total,"dollars.")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    answer = input("Do you want to calculate the cost of another trip?: ")
    if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
        continue
    else:
        print("Have a good trip!")
        break

"""
