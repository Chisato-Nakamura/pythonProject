print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure")

road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.\n")
low_road = road.lower()
if low_road == "left":

    lake = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    low_lake = lake.lower()
    if low_lake == "wait":

        island = input(
            "You arrive at the island unharmed. There is a house with 3 dorrs. One re, one yellow and one blue. Which colour do you choose?\n")
        low_island = island.lower()
        if low_island == "yellow":
            print("You Win!")
        elif low_island == "red":
            print("Burned by fire. Game Over.")
        elif low_island == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")

    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over.")
