#QUIZ

print("This is a quiz that tests your knowlege of Frank Ocean.")

name= input("Enter your name: ")
print("Are you ready to begin?")
print("Each question will have three possible answers")

#Set the score to 0

score = 0
score= int(score)

#Question One

print("When is Frank Oceans birthday?")
print("A. September 25th")
print("B. October 28th")
print("C. November 30th")

Q1answer = "October 28th" #Correct Answer
Q1response = input("Your answer: ")

if Q1response == "b" or Q1response == "B":
    print("Correct!")
    score = score + 1
elif Q1response != "b" or Q1response != "B":
    print("Answer is incorrect. Correct answer is: ",Q1answer)
    score = score + 0

#Question Two

print("How many studio albums does Frank Ocean have?")
print("A. 2")
print("B. 3")
print("C. 4")

Q2answer = "2" #Correct Answer
Q2response = input("Your answer: ")

if Q2response == "a" or Q2response == "A":
    print("Correct!")
    score = score + 1
elif Q2response != "a" or Q2response != "A":
    print("Answer is incorrect. Correct answer is: ",Q2answer)
    score = score + 0

#Question Three

print("How many siblings does Frank Ocean have?")
print("A. 0")
print("B. 1")
print("C. 2")

Q3answer = "2" #Correct Answer
Q3response = input("Your answer: ")

if Q3response == "c" or Q3response == "C":
    print("Correct!")
    score = score + 1
elif Q3response != "c" or Q3response != "C":
    print("Answer is incorrect. Correct answer is: ",Q3answer)
    score = score + 0

#Question Four

print("What is Frank Oceans most recent song?")
print("A. Biking")
print("B. Provider")
print("C, Lens")

Q4answer = "Provider" #Correct Answer
Q4response = input("Your answer: ")

if Q4response == "b" or Q4reponse == "B":
    print("Correct!")
    score = score + 1
elif Q4response != "b" or Q4response != "B":
    print("Answer is incorrect. Correct answer is: ",Q4answer)
    score = score + 0
    
#Question Five

print("What is track 10 on Channel Orange?")
print("A. Forrest Gump")
print("B. Pyramids")
print("C. Super Rich Kids")

Q5answer = "Pyramids" #Correct Answer
Q5response= input("Your answer: ")

if Q5response == "b" or Q5response == "B":
    print("Correct!")
    score = score + 1
elif Q5response != "b" or Q5response != "B":
    print("Answer is incorrect. Correct answer is: ",Q5answer)

#Question Six

print("How many tracks are on Blonde?")
print("A. 15")
print("B. 16")
print("C. 17")

Q6answer = "16" #Correct Answer
Q6response = input("Your answer: ")

if Q6response == "c" or Q6response == "C":
    print("Correct!")
    score = score + 1
elif Q6response != "c" or Q6reponse != "C":
    print("Answer is incorrect. Correct answer is: ",Q6answer)

print("Your score is: ",(score/6)*100)
