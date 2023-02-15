#Create a program using maths and f-Strings that tells us how many days, weeks, months
#we have left if we live until 90 years old.

age = input("What is your current age? ")

#Total number of days, weeks and months of your entire life
life_days = int(90*365)
life_weeks = int(90*52)
life_month  = int(90*12)

#Overwrite string 'age' to integer
age = int(age)

#Subtract days, weeks and months that you've spent from the total number
day = life_days - age * 365
week = life_weeks - age * 52
month = life_month - age * 12

print(f"You have {day} days, {week} weeks, and {month} months left.")

