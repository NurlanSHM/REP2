# Python Random Num guessing game
import random

lownum = 1
highnum = 100
answer = random.randint(lownum, highnum)
guesses = 0
is_running = True

print("Python number guesing game")
print(f"Select a number between {lownum} and {highnum}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        pass
    else:
        print("Invalid Guess!")
        print(f"Please select a number between {lownum} and {highnum}")