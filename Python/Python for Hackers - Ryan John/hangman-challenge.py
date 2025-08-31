import random 

game_over = False
num = 0

print("Welcome to the Hangman")

words = ["hacker", "activism", "random"]

secret_word = random.choice(words)
print(secret_word) # testing proposes
display_word = []

for letter in secret_word:
    display_word += "-" # increment
print(display_word)



while not game_over:
    guess = input("Guess a letter: ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter    
    if guess  not in secret_word:
        guesses_left = 5 - num
        print(f"Gueeses left: {guesses_left}")
        num += 1
        if num >= 5:
            print("You lose")
            game_over = True
    print(display_word)
    
    if "-" not in display_word:
        print("You win")
        game_over = True