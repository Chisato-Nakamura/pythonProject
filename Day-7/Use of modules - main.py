#Step 4
from replit import clear
import random
import hangman_art
import hangman_words

#print hangman logo
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  while True:
    guess = input("Guess a letter: ").lower()
    clear() #clear the screen everytime user guessed a letter
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
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  #If display doesn't contain a blank print"You win." 
  if "_" not in display:
    end_of_game = True
    print("You win.")
    
  print(hangman_art.stages[lives])
  
