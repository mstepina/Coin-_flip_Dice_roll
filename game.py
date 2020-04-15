"""

Basic console application that allows the user to guess 
the outcome of a random coin flip or dice roll

"""

import time, random

def coin_flip():
    global correct
    global total
    global start
    print(f"Your score is {correct} out of {total}")
    guess_coin = input("Heads or tails? >>> ").lower().replace(" ", "")
    print("Let's flip it...")
    time.sleep(1)
    flip_res_n = random.randint(1, 2)
    if flip_res_n == 1:
        flip_res = "tails"
    else:
        flip_res = "heads"
    print(f"It lands on... {flip_res}")
    time.sleep(1)
    if guess_coin == flip_res:
        print ("Good job! You guessed right")
        correct += 1
    else:
        print ("You guessed wrong. Try again!")
    total += 1
    start = input("Another game? yes/no >>> ").replace(" ", "")

def roll_dice():
    global correct
    global total
    global start
    print(f"Your score is {correct} out of {total}")
    guess_dice = input("Your guess for dice? 1-6 >>> ").lower().replace(" ", "")
    print("Let's roll it...")
    time.sleep(1)
    dice_res = random.randint(1, 6)
    print(f"The result is... {dice_res}")
    time.sleep(1)
    if int(guess_dice) == dice_res:
        print ("Good job! You guessed right")
        correct += 1
    else:
        print ("You guessed wrong. Try again!")
    total += 1
    start = input("Another game? yes/no >>> ").replace(" ", "")

start = input("Ready to start? yes/no >>> ").lower().replace(" ", "")
total = 0
correct = 0
while start == "yes":
    game = input("Choose a game: Coin flip or dice roll? >>> ").lower().replace(" ", "")
    #print(game)
    if game == "coinflip":
        coin_flip()
    elif game == "diceroll":
        roll_dice()
    else:
        print("Something wrong. Try again")
        start = input("Ready to start? yes/no >>> ").lower().replace(" ", "")


