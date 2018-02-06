#QUIZ

print("This is a quiz that tests your knowlege of Frank Ocean.")

while True:
    name= input("Enter your name: ")
    print("Are you ready to begin",name,"?")
    print("Each question will have three possible answers, A, B or C.")

#Set the score to 0

    score = 0
    score= int(score)
    print("------------------------------------------------------")
#Question One
    print("QUESTION ONE")
    print("")
    print("When is Frank Oceans birthday?")
    print("A. September 25th")
    print("B. October 28th")
    print("C. November 30th")
    print("")
    Q1response = input("Your answer: ")
    print("")
    if Q1response == "b" or Q1response == "B":
        print("Correct!")
        score = score + 1
    elif Q1response != "b" or Q1response != "B":
        print("Answer is incorrect.")
        score = score + 0
    print("------------------------------------------------------")
#Question Two
    print("QUESTION TWO")
    print("")
    print("How many studio albums does Frank Ocean have?")
    print("A. 2")
    print("B. 3")
    print("C. 4")
    print("")
    Q2response = input("Your answer: ")
    print("")
    if Q2response == "a" or Q2response == "A":
        print("Correct!")
        score = score + 1
    elif Q2response != "a" or Q2response != "A":
        print("Answer is incorrect.")
        score = score + 0
    print("------------------------------------------------------")
#Question Three
    print("QUESTION THREE")
    print("")
    print("How many siblings does Frank Ocean have?")
    print("A. 0")
    print("B. 1")
    print("C. 2")
    print("")
    Q3response = input("Your answer: ")
    print("")
    if Q3response == "c" or Q3response == "C":
        print("Correct!")
        score = score + 1
    elif Q3response != "c" or Q3response != "C":
        print("Answer is incorrect.")
        score = score + 0
    print("------------------------------------------------------")
#Question Four
    print("QUESTION FOUR")
    print("")
    print("What is Frank Oceans most recent song?")
    print("A. Biking")
    print("B. Provider")
    print("C. Lens")
    print("")
    Q4response = input("Your answer: ")
    print("")
    if Q4response == "b" or Q4response == "B":
        print("Correct!")
        score = score + 1
    elif Q4response != "b" or Q4response != "B":
        print("Answer is incorrect.")
        score = score + 0
    print("------------------------------------------------------")
#Question Five
    print("QUESTION FIVE")
    print("")
    print("What is track 10 on Channel Orange?")
    print("A. Forrest Gump")
    print("B. Pyramids")
    print("C. Super Rich Kids")
    print("")
    Q5response= input("Your answer: ")
    if Q5response == "b" or Q5response == "B":
        print("Correct!")
        score = score + 1
    elif Q5response != "b" or Q5response != "B":
        print("Answer is incorrect.")
    print("------------------------------------------------------")
#Question Six
    print("QUESTION SIX")
    print("")
    print("How many tracks are on Blonde?")
    print("A. 15")
    print("B. 16")
    print("C. 17")
    print("")
    Q6response = input("Your answer: ")
    if Q6response == "c" or Q6response == "C":
        print("Correct!")
        score = score + 1
    elif Q6response != "c" or Q6response != "C":
        print("Answer is incorrect.")
    print("")
    print("Final score:",score,"out of 6")
    print("------------------------------------------------------")
    score = (score/6)*100
    if score >= 75.0:
        print("Congratulations",name,"!","You got",round(score,0),"right!")
    else:
        print("Sorry",name,":( Your score is:",round(score,0), "percent")
    answer = input("Do you want to take this quiz again? ")
    if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
        continue
    else:
        break
