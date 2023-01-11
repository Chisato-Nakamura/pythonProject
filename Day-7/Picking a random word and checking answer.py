import random

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while True:
    guess = input("Guess a letter: ").lower()
    n = len(guess)
    if n == 1:
        break #a

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if guess in chosen_word:
    print("Matched")
else:
    print("Doesn't match")