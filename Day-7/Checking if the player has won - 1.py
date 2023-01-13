# Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while True:
    while True:
        guess = input("Guess a word: ")
        count = len(guess)
        if count == 1:
            break

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    print(display)

    if "_" not in display:
        print("You win.")
        break
