# Shadow Treasure Game

import random

print("Shadow Treasure Game")
print("Find the hidden treasure box")

box = random.randint(1,5)
chance = 3

while chance > 0:
    guess = int(input("Choose box number (1-5): "))

    if guess == box:
        print("Treasure Found! You Win")
        break

    else:
        chance = chance - 1
        print("Wrong Box")

        if guess < box:
            print("Treasure is in higher box")
        else:
            print("Treasure is in lower box")

        print("Chances Left:", chance)

if chance == 0:
    print("Game Over")
    print("Treasure was in box:", box)