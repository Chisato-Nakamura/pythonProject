#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while True:
  while True:
    guess = input("Guess a letter: ").lower()
    count = len(guess)
    if count == 1:
      break
  
  #Check guessed letter
  #Specify the position where the letter needs to be replaced
  for position in range(word_length):
    if guess == chosen_word[position]:
      display[position] = guess

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  
  #If guess is not a letter in the chosen_word, then reduce 'lives' by 1. 
  if guess not in chosen_word:
    lives -= 1

  #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(stages[lives])

  #If display doesn't contain a blank print"You win." 
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if "_" not in display:
    print("You win.")
    break
  elif lives == 0:
    print("You lose.")
    break
