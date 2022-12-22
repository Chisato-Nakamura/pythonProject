#write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.


import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#e.g.) names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
length = len(names) - 1

#generate a random number btw 0 to the length -1 of the list
person_random = random.randint(0,length)

print(f"{names[person_random]} is going to buy the meal today!")


