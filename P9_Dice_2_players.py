import random

def dice_roll():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

player1 = input("Enter player one's name : ")
player2 = input("Enter player two's name : ")

roll1 = dice_roll()
roll2 = dice_roll()

print(player1, "rolled", roll1)
print(player2, "rolled", roll2)

if roll1 > roll2:
    print(player1, "WINS")
elif roll2 > roll1:
    print(player2, "WINS")
else:
    print("It's a TIE")

# Enter player one's name : Kevin Hart
# Enter player two's name : The Rock
# Kevin Hart rolled 5
# The Rock rolled 6
# The Rock WINS