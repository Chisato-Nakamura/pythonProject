print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

person1 = name1.lower()
person2 = name2.lower()

both_name = person1 + person2 #combine names

t = both_name.count("t")
r = both_name.count("r")
u = both_name.count("u")
e = both_name.count("e")

l = both_name.count("l")
o = both_name.count("o")
v = both_name.count("v")
e = both_name.count("e")

#add up all numbers and change int to string
true = str(t+r+u+e)
love = str(l+o+v+e)

#put the both string together and change it to integer
true_love = int(true+love)

if true_love <10 or true_love >90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")

elif true_love >=40 and true_love <=50:
    print(f"Your score is {true_love}, you are alright together.")

else:
    print(f"Your score is {true_love}.")



