import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Your choice - rock, paper or scissors ?? : ").lower()

if computer_choice == user_choice:
    print(f"It's a TIE!!! Both choose {computer_choice}")
elif user_choice == "rock" and computer_choice == "scissors":
    print(f"You WIN!!! Computer choose {computer_choice}")
elif user_choice == "paper" and computer_choice == "rock":
    print(f"You WIN!!! Computer choose {computer_choice}")
elif user_choice == "scissors" and computer_choice == "paper":
    print(f"You WIN!!! Computer choose {computer_choice}")
else:
    print(f"You LOSE :( Computer choose {computer_choice}")


# Your choice - rock, paper or scissors ?? : paper
# You WIN!!! Computer choose rock

# Your choice - rock, paper or scissors ?? : scissors
# It's a TIE!!! Both choose scissors

# Your choice - rock, paper or scissors ?? : rock
# You LOSE :( Computer choose paper