import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for _ in chosen_word:
    display += "_"
print(display)

#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
while True:
    guess = input("Guess a word: ")
    count = len(guess)
    if count == 1:
        break

for position in range(len(chosen_word)):
    if guess == chosen_word[position]:
        display[position] = guess

#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)