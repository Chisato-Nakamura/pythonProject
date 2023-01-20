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
print("You chose:")
print(rps[choice])
 
 
print("Computer chose:")
 
random_computer = random.randint(0,2)
computer = rps[random_computer]
print(computer)
 
if (choice == 0) and (random_computer == 0):
  print("Draw")
elif (choice == 0) and (random_computer == 1):
  print("You lose")
elif (choice == 0) and (random_computer == 2):
   print("You win")
elif (choice == 1) and (random_computer == 0):
  print("You win")
elif (choice == 1) and (random_computer == 1):
  print("Draw")
elif (choice == 1) and (random_computer == 2):
  print("You lose")
elif (choice == 2) and (random_computer == 0):
  print("You lose")
elif (choice == 2) and (random_computer == 1):
  print("You win")
else:
  print("Draw")

print("-")
