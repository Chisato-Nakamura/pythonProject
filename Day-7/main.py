import random
import hangman_art
import hangman_words
from replit import clear

# print logo
print(hangman_art.logo)

# generate a random word
random_word = random.choice(hangman_words.word_list)
print(hangman_art.stages[6])

# generate as many blanks as letters in word
num_letter = ""
letter_list = []
for x in range(len(random_word)):
    num_letter += "_"
    letter_list += "_"
print(num_letter)

life = 6
end_of_game = False
while end_of_game == False:
    # Ask the user to guess a letter
    while end_of_game == False:
      letter = input("Guess a letter: ").lower()
      clear()
      count = len(letter)
      if count == 1:
        break
      else:
        print("Choose ONLY ONE letter.")
      
    # check if the guessed letter in the word
    count = 0
    if letter in letter_list:
      print(f"You've already gussed {letter}")
      
    for x in range(len(random_word)):
        if random_word[x] == letter:
            letter_list[x] = letter
            count += 1 
  
    if count == 0:
      life -= 1
      print(f"You gussed {letter}, that's not in the word. you lose a life.")

    print(''.join(letter_list))
    print(hangman_art.stages[life])
    
  
    if '_' not in ''.join(letter_list):
      print("You win")
      end_of_game = True
    elif life == 0:
      end_of_game = True
      print(f"Game Over. The answer is: {random_word}.")
