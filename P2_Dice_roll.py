import random

roll = random.randint(1, 6)
guess = int(input("Guess the dice roll : "))

if guess == roll:
    print(f"You gussed right!! The roll was {roll}")
else:
    print(f"Sorry :(  The roll was {roll}")