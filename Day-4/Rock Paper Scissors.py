# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# user_input = " "

# while True:
rps = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"You chose:\n {rps[choice]}")
 

random_computer = random.randint(0,2)
print(f"Computer chose:\n {rps[random_computer]}")


#user chose 0
if choice == 0:
  if random_computer == 0:
    print("Draw")
  elif random_computer == 1:
    print("Lose")
  else:
    print("You win")
    
#user chose 1
if choice == 1:
  if random_computer == 0:
    print("Win")
  elif random_computer == 1:
    print("Draw")
  else:
    print("Lose")

#user chose 2
if choice == 2:
  if random_computer == 0:
    print("Lose")
  elif random_computer == 1:
    print("Win")
  else:
    print("Draw")

print("-")
