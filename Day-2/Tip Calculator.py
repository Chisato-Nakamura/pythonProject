#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many pople to split the bill? "))


#get the percentage of tip
if tip == 10:
  new_tip = 10/100
elif tip == 12:
  new_tip = 12/100
elif tip == 15:
  new_tip = 15/100
else:
  print("Please select either 10%, 12% or 15%")

tip_percentage = 1 + new_tip #either 1.1, 1.12or 1.15

#Total
new_total = round((total / people) * tip_percentage, 2)
print(f"Each person should pay: ${new_total}")