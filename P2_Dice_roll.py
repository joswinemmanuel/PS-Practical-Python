import random

roll = random.randint(1, 6)
guess = int(input("Guess the dice roll : "))

if guess == roll:
    print(f"You guessed right!! The roll was {roll}")
else:
    print(f"Sorry :(  The roll was {roll}")


# Guess the dice roll : 6
# Sorry :(  The roll was 5

# Guess the dice roll : 3
# You guessed right!! The roll was 3