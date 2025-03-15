import random

low = 1
high = 120
options = ("Rock", "Paper", "Scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low,high)
# number = random.random()
# option = random.choice(options)
random.shuffle(cards)

print(cards)
