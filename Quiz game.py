# Python quiz game
import time

questions = (("What is the formula for refractive index?"),
           ("When did WWII begin?"),
           ("What is the most abundant gas on earth?"),
           ("Which of the following is a 5th generation fighter jet?"),
           ("How many bones in the human body?"))

options = (("A. sin(r)/sin(i)", "B. sin(i)/sin(r)", "C. sinc/n", "D. what is refractive index bro?"),
           ("A. 1938", "B. 1940", "C. 1945", "D. 1939"),
           ("A. Nitrogen ", "B. Hydrogen ", "C. Oxygen", "D. CO2"),
           ("A. F18A", "B. Su-57", "C. F15E", "D. MiG-31"),
           ("A. 205 ", "B. 207", "C. 206", "D. 201"))

answers = ("A","D", "A","B","C")
guesses = []
score = 0
question_num = 0

for q in questions:
    time.sleep(1)
    print("----------------")
    print(q)
    for op in options[question_num]:
        print(op)
    
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        time.sleep(0.5)
        print("Correct!")
    
    else:
        time.sleep(0.75)
        print("Incorrect!")
        time.sleep(0.75)
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("  R  E  S  U  L  T  S ")
print("----------------------")

print("Answers: ", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

print("Guesses: ", end=" ")
for g in guesses:
    print(g, end=" ")
print()

score = (score / len(questions) * 100)
print(f"Your score is: {score:.0f}%")